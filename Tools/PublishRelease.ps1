param([string]$Tag='v1.0.1')
$ErrorActionPreference='Stop'
$project=[IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$repository='medissl/April-again'
$api="https://api.github.com/repos/$repository"
$artifacts=@('AprilAgain-Setup.exe','AprilAgain-Windows.zip','SHA256SUMS.txt')
foreach($name in $artifacts){if(-not(Test-Path -LiteralPath (Join-Path $project "Builds/$name"))){throw "Missing release artifact: $name"}}
$notes=Get-Content -LiteralPath (Join-Path $project 'Documentation/ReleaseNotes.md') -Raw
$env:GCM_INTERACTIVE='Never';$env:GIT_TERMINAL_PROMPT='0'
# Credentials stay in memory; never write them into command arguments, logs or files.
$credentialLines="protocol=https`nhost=github.com`n`n" | git credential fill 2>$null
$credentialFields=@{}
foreach($line in $credentialLines){if($line -match '^([^=]+)=(.*)$'){$credentialFields[$matches[1]]=$matches[2]}}
if(-not $credentialFields['password']){throw 'Git Credential Manager has no GitHub credential.'}
$headers=@{Authorization='Bearer '+$credentialFields['password'];Accept='application/vnd.github+json';'X-GitHub-Api-Version'='2026-03-10'}
try{
    $release=$null
    try{$release=Invoke-RestMethod -Uri "$api/releases/tags/$Tag" -Headers $headers}catch{if([int]$_.Exception.Response.StatusCode -ne 404){throw}}
    if(-not $release){
        $commit=(git -C $project rev-parse HEAD).Trim()
        $body=@{tag_name=$Tag;target_commitish=$commit;name=('April, again '+$Tag.TrimStart('v'));body=$notes;draft=$true;prerelease=$false}|ConvertTo-Json
        $release=Invoke-RestMethod -Uri "$api/releases" -Method Post -Headers $headers -ContentType 'application/json; charset=utf-8' -Body ([Text.Encoding]::UTF8.GetBytes($body))
    }
    elseif($release.draft){
        $body=@{target_commitish=(git -C $project rev-parse HEAD).Trim();body=$notes}|ConvertTo-Json
        $release=Invoke-RestMethod -Uri "$api/releases/$($release.id)" -Method Patch -Headers $headers -ContentType 'application/json; charset=utf-8' -Body ([Text.Encoding]::UTF8.GetBytes($body))
    }
    foreach($name in $artifacts){
        $path=Join-Path $project "Builds/$name";$hash=(Get-FileHash -LiteralPath $path -Algorithm SHA256).Hash.ToLowerInvariant()
        $asset=@($release.assets | Where-Object name -EQ $name)
        if($asset.Count){
            if($asset[0].size -eq (Get-Item -LiteralPath $path).Length -and $asset[0].digest -eq "sha256:$hash"){continue}
            if(-not $release.draft){throw "A different published release asset exists: $name"}
            Invoke-RestMethod -Uri "$api/releases/assets/$($asset[0].id)" -Method Delete -Headers $headers | Out-Null
        }
        if(-not $release.draft){throw 'Refusing to modify a published release with missing artifacts.'}
        $uri=($release.upload_url -replace '\{.*$','')+'?name='+[Uri]::EscapeDataString($name)
        $uploaded=Invoke-RestMethod -Uri $uri -Method Post -Headers $headers -ContentType 'application/octet-stream' -InFile $path -TimeoutSec 1800
        if($uploaded.size -ne (Get-Item -LiteralPath $path).Length -or $uploaded.digest -ne "sha256:$hash"){throw "Upload verification failed: $name"}
        Write-Output "Verified upload: $name ($($uploaded.size) bytes)"
    }
    $published=Invoke-RestMethod -Uri "$api/releases/$($release.id)" -Method Patch -Headers $headers -ContentType 'application/json' -Body '{"draft":false,"make_latest":"true"}'
    $published | Select-Object html_url,tag_name,published_at,@{n='assets';e={$_.assets | Select-Object name,size,digest,browser_download_url}} | ConvertTo-Json -Depth 5
}finally{
    $headers.Clear();$credentialFields.Clear();$credentialLines=$null
}
