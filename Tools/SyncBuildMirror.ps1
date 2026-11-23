param([switch]$PullGenerated)
$ErrorActionPreference='Stop'
$sourceProject=[IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$mirrorProject=(Get-Content -LiteralPath (Join-Path $sourceProject 'Documentation/Testing/build-mirror-path.txt') -Raw).Trim()
$mirrorProject=[IO.Path]::GetFullPath($mirrorProject)
$temporaryRoot=[IO.Path]::GetFullPath((Join-Path $env:USERPROFILE 'AppData/Local/Temp'))
if(-not $mirrorProject.StartsWith($temporaryRoot,[StringComparison]::OrdinalIgnoreCase)){throw 'Unexpected build mirror path.'}
$owner=(Get-Content -LiteralPath (Join-Path $mirrorProject '.april-build-mirror.txt') -Raw).Trim()
if($owner -ne $sourceProject){throw 'Build mirror belongs to a different source project.'}
function Copy-RelativeFile([string]$from,[string]$to,[string]$relative){
    $target=Join-Path $to $relative
    $inputFile=Join-Path $from $relative
    if((Test-Path -LiteralPath $target) -and ((Get-FileHash -LiteralPath $inputFile).Hash -eq (Get-FileHash -LiteralPath $target).Hash)){return}
    New-Item -ItemType Directory -Path (Split-Path -Parent $target) -Force | Out-Null
    Copy-Item -LiteralPath $inputFile -Destination $target -Force
}
if($PullGenerated){
    foreach($file in Get-ChildItem -LiteralPath (Join-Path $mirrorProject 'Assets') -Filter '*.meta' -File -Recurse){
        $relative=$file.FullName.Substring($mirrorProject.Length+1)
        $sourceMeta=Join-Path $sourceProject $relative
        if(Test-Path -LiteralPath $sourceMeta){
            $original=Get-Content -LiteralPath $sourceMeta -Raw
            $prepared=Get-Content -LiteralPath $file.FullName -Raw
            $originalGuid=[regex]::Match($original,'(?m)^guid: (.+)$').Groups[1].Value.Trim()
            $preparedGuid=[regex]::Match($prepared,'(?m)^guid: (.+)$').Groups[1].Value.Trim()
            if($originalGuid -ne $preparedGuid){throw "Refusing to replace a different asset GUID: $relative"}
            if($original -eq $prepared){continue}
            $backup=Join-Path $sourceProject ('Documentation/Testing/SourceMetaBackup/'+$relative)
            if(-not(Test-Path -LiteralPath $backup)){
                New-Item -ItemType Directory -Path (Split-Path -Parent $backup) -Force | Out-Null
                Copy-Item -LiteralPath $sourceMeta -Destination $backup
            }
        }
        Copy-RelativeFile $mirrorProject $sourceProject $relative
    }
    foreach($relative in @('Assets/AprilAgain/GameData/GameCatalog.asset','Assets/AprilAgain/GameData/NunitoDefaultFont.asset','Assets/TextMesh Pro/Resources/TMP Settings.asset','Assets/Scenes/AprilAgain.unity','ProjectSettings/ProjectSettings.asset','ProjectSettings/EditorBuildSettings.asset')){
        if(Test-Path -LiteralPath (Join-Path $mirrorProject $relative)){Copy-RelativeFile $mirrorProject $sourceProject $relative}
    }
    $reportSource=Join-Path $mirrorProject 'Documentation/Testing'
    if(Test-Path -LiteralPath $reportSource){
        $reportTarget=Join-Path $sourceProject 'Documentation/Testing/Presentation'
        New-Item -ItemType Directory -Path $reportTarget -Force | Out-Null
        Copy-Item -Path (Join-Path $reportSource '*') -Destination $reportTarget -Recurse -Force
    }
    Write-Output 'Pulled generated catalog, font assets, new metadata and verification records.'
}else{
    foreach($folder in @('Assets/AprilAgain/Scripts','Assets/AprilAgain/Editor','Assets/AprilAgain/Art/UI/Spring','Assets/AprilAgain/Art/UI/Final','Assets/AprilAgain/Art/Fonts/Nunito','Assets/AprilAgain/Art/Title','Assets/AprilAgain/Audio/World')){
        foreach($file in Get-ChildItem -LiteralPath (Join-Path $sourceProject $folder) -File -Recurse){
            $relative=$file.FullName.Substring($sourceProject.Length+1)
            if($file.Extension -eq '.meta' -and (Test-Path -LiteralPath (Join-Path $mirrorProject $relative))){continue}
            Copy-RelativeFile $sourceProject $mirrorProject $relative
        }
    }
    foreach($folder in Get-ChildItem -LiteralPath (Join-Path $sourceProject 'Assets/AprilAgain/Art/Characters') -Directory){
        $conversation=Join-Path $folder.FullName 'Conversation'
        if(Test-Path -LiteralPath $conversation){foreach($file in Get-ChildItem -LiteralPath $conversation -File){
            $relative=$file.FullName.Substring($sourceProject.Length+1)
            if($file.Extension -eq '.meta' -and (Test-Path -LiteralPath (Join-Path $mirrorProject $relative))){continue}
            Copy-RelativeFile $sourceProject $mirrorProject $relative
        }}
    }
    Copy-RelativeFile $sourceProject $mirrorProject 'Assets/AprilAgain/GameData/content.json'
    Write-Output 'Updated mirror source, UI, fonts, conversation sprites and compiled content.'
}
