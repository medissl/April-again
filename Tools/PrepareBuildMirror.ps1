param([string]$MirrorPath)
$ErrorActionPreference = 'Stop'
$sourceProject = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$temporaryRoot = [IO.Path]::GetFullPath((Join-Path $env:USERPROFILE 'AppData/Local/Temp'))
if (-not $MirrorPath) {
    $mirrorName = 'AprilAgainBuild_' + [DateTime]::Now.ToString('yyyyMMdd_HHmmss')
    $MirrorPath = Join-Path $temporaryRoot $mirrorName
}
$MirrorPath = [IO.Path]::GetFullPath($MirrorPath)
if (-not $MirrorPath.StartsWith($temporaryRoot, [StringComparison]::OrdinalIgnoreCase) -or $MirrorPath.Contains(',')) {
    throw 'Build mirrors must be new comma-free directories inside the system temporary directory.'
}
if (Test-Path -LiteralPath $MirrorPath) { throw 'The mirror destination already exists. Use a new directory.' }
New-Item -ItemType Directory -Path $MirrorPath | Out-Null
foreach ($folder in @('Assets','Packages','ProjectSettings')) {
    Copy-Item -LiteralPath (Join-Path $sourceProject $folder) -Destination $MirrorPath -Recurse
}
Copy-Item -LiteralPath (Join-Path $sourceProject 'DESIGN.md') -Destination $MirrorPath
Set-Content -LiteralPath (Join-Path $MirrorPath '.april-build-mirror.txt') -Value $sourceProject
Set-Content -LiteralPath (Join-Path $sourceProject 'Documentation/Testing/build-mirror-path.txt') -Value $MirrorPath
Write-Output $MirrorPath
