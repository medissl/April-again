param([string]$Compiler)
$ErrorActionPreference='Stop'
$project=[IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
if(-not $Compiler){$Compiler=Join-Path $PSScriptRoot 'Local/nsis-3.11/makensis.exe'}
if(-not(Test-Path -LiteralPath $Compiler)){throw 'Provide -Compiler pointing to a local NSIS 3 makensis.exe.'}
if(-not(Test-Path -LiteralPath (Join-Path $project 'Builds/Windows/AprilAgain.exe'))){throw 'Package the checked Windows player first.'}
& $Compiler /V2 ("/DPROJECT_ROOT="+$project) (Join-Path $PSScriptRoot 'Installer.nsi')
if($LASTEXITCODE -ne 0){throw 'Installer compilation failed.'}
Get-FileHash -LiteralPath (Join-Path $project 'Builds/AprilAgain-Setup.exe') | Select-Object Hash,Path
