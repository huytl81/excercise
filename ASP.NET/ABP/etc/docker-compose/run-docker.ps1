$currentFolder = $PSScriptRoot

$certsFolder = Join-Path $currentFolder "certs"

If(!(Test-Path -Path $certsFolder))
{
    New-Item -ItemType Directory -Force -Path $certsFolder
    if(!(Test-Path -Path (Join-Path $certsFolder "localhost.pfx") -PathType Leaf)){
        Set-Location $certsFolder
        dotnet dev-certs https -v -ep localhost.pfx -p fe667b70-a174-4cd7-a93d-7d264e0a8da7 -t        
    }
}

Set-Location $currentFolder
docker-compose up -d
exit $LASTEXITCODE