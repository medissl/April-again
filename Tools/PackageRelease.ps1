param([switch]$SkipZip)
$ErrorActionPreference='Stop'
$sourceProject=[IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$mirrorProject=(Get-Content -LiteralPath (Join-Path $sourceProject 'Documentation/Testing/build-mirror-path.txt') -Raw).Trim()
$mirrorProject=[IO.Path]::GetFullPath($mirrorProject)
$temporaryRoot=[IO.Path]::GetFullPath((Join-Path $env:USERPROFILE 'AppData/Local/Temp'))
if(-not $mirrorProject.StartsWith($temporaryRoot+[IO.Path]::DirectorySeparatorChar,[StringComparison]::OrdinalIgnoreCase)){throw 'Unexpected build mirror.'}
if((Get-Content -LiteralPath (Join-Path $mirrorProject '.april-build-mirror.txt') -Raw).Trim() -ne $sourceProject){throw 'Build mirror owner mismatch.'}
$build=Join-Path $mirrorProject 'Builds/Windows'
if(-not(Test-Path -LiteralPath (Join-Path $build 'AprilAgain.exe'))){throw 'No built Windows player.'}
$buildRoot=Join-Path $sourceProject 'Builds'
$release=[IO.Path]::GetFullPath((Join-Path $buildRoot 'Windows'))
$prefix=[IO.Path]::GetFullPath($buildRoot)+[IO.Path]::DirectorySeparatorChar
function Assert-BuildPath([string]$path){if(-not [IO.Path]::GetFullPath($path).StartsWith($prefix,[StringComparison]::OrdinalIgnoreCase)){throw 'Build destination escaped the workspace.'}}
Assert-BuildPath $release
if(Test-Path -LiteralPath $release){
    $previous=Join-Path $buildRoot ('Previous-Windows-'+[DateTime]::UtcNow.ToString('yyyyMMdd-HHmmss'))
    Assert-BuildPath $previous
    Move-Item -LiteralPath $release -Destination $previous
}
New-Item -ItemType Directory -Path $release -Force | Out-Null
foreach($item in Get-ChildItem -LiteralPath $build){
    if($item.Name -match 'DoNotShip|BackUpThisFolder'){continue}
    Copy-Item -LiteralPath $item.FullName -Destination $release -Recurse
}
$legal=Join-Path $release 'Legal'
New-Item -ItemType Directory -Path $legal | Out-Null
Copy-Item -LiteralPath (Join-Path $sourceProject 'Assets/AprilAgain/Art/Fonts/Nunito/OFL.txt') -Destination (Join-Path $legal 'Nunito-OFL.txt')
Copy-Item -LiteralPath (Join-Path $sourceProject 'Documentation/AudioSources/Licenses/Kenney-Interface-Sounds.txt') -Destination (Join-Path $legal 'Kenney-Interface-Sounds.txt')
Copy-Item -LiteralPath (Join-Path $sourceProject 'Documentation/AudioSources/Licenses/Kenney-RPG-Audio.txt') -Destination (Join-Path $legal 'Kenney-RPG-Audio.txt')
Copy-Item -LiteralPath (Join-Path $sourceProject 'Documentation/AudioSources/Rain-License.txt') -Destination (Join-Path $legal 'Rain-License.txt')
Copy-Item -LiteralPath (Join-Path $sourceProject 'Documentation/ThirdParty/NSIS.txt') -Destination (Join-Path $legal 'NSIS.txt')
@'
April, again
Created by Medissl, with Codex / OpenAI production tools.

Original game illustrations, screenplay and music were made for this project.
MENFENG menu hover/select/open cues are reused with their creator's permission.
Additional interface effects: Kenney Interface Sounds (CC0).
https://kenney.nl/assets/interface-sounds
Door recording: Kenney RPG Audio (CC0).
https://kenney.nl/assets/rpg-audio
Rain on Window Loop: alxl (CC0 license option).
https://opengameart.org/content/rain-on-window-loop

Typeface: Nunito, copyright the Nunito Project Authors, SIL Open Font License 1.1.
Static ExtraBold instance from the official variable font, prepared with FontTools.
https://github.com/googlefonts/nunito
The font and Kenney license notices are included in Legal.
'@ | Set-Content -LiteralPath (Join-Path $release 'CREDITS.txt') -Encoding utf8
@'
April, again

Run AprilAgain.exe. Keep AprilAgain_Data, MonoBleedingEdge and UnityPlayer.dll beside it.

Click or Space: reveal / advance dialogue. Escape: menu. H: hide the interface.
F5: quick save. F9: quick load. Skip stops at unread text and choices.

Use doors or the map to travel; travel and inspection are free.
On the first day, notice all five classmates before heading home.
Later days have two three-hour activity blocks; Saturday has three. Sunday is a rest day.
Each classmate has one story encounter per day. Check the journal for appointments.
The fifteenth encounter finishes a route and the playthrough. A pre-finale save is kept.

Saves are stored in AppData/LocalLow/Medissl/April, again/AprilAgain.
'@ | Set-Content -LiteralPath (Join-Path $release 'README.txt') -Encoding utf8
$files=Get-ChildItem -LiteralPath $release -File -Recurse
if($files.Name -contains 'autosave.json' -or $files.Name -contains 'preferences.json'){throw 'QA progress must not be packaged.'}
$proof=@{
    target='Windows x64';version='1.0.0';packagedUtc=[DateTime]::UtcNow.ToString('o')
    executable='Builds/Windows/AprilAgain.exe';executableBytes=(Get-Item -LiteralPath (Join-Path $release 'AprilAgain.exe')).Length
    files=$files.Count;totalBytes=($files | Measure-Object -Property Length -Sum).Sum
    contentSha256=(Get-FileHash -LiteralPath (Join-Path $sourceProject 'Assets/AprilAgain/GameData/content.json')).Hash
    fontSha256=(Get-FileHash -LiteralPath (Join-Path $sourceProject 'Assets/AprilAgain/Art/Fonts/Nunito/Nunito-ExtraBold.ttf')).Hash
}
if(-not $SkipZip){
    $zip=Join-Path $buildRoot 'AprilAgain-Windows.zip';Assert-BuildPath $zip
    if(Test-Path -LiteralPath $zip){
        $oldZip=Join-Path $buildRoot ('Previous-Windows-'+[DateTime]::UtcNow.ToString('yyyyMMdd-HHmmss')+'.zip');Assert-BuildPath $oldZip
        Move-Item -LiteralPath $zip -Destination $oldZip
    }
    Compress-Archive -Path (Join-Path $release '*') -DestinationPath $zip -CompressionLevel Optimal
    $proof.zip='Builds/AprilAgain-Windows.zip';$proof.zipBytes=(Get-Item -LiteralPath $zip).Length
    $proof.zipSha256=(Get-FileHash -LiteralPath $zip).Hash
}
$proof | ConvertTo-Json | Set-Content -LiteralPath (Join-Path $sourceProject 'Documentation/Testing/release-package.json') -Encoding utf8
Write-Output ($proof | ConvertTo-Json -Compress)
