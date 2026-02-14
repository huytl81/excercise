param ($version='latest')

$currentFolder = $PSScriptRoot
$slnFolder = Join-Path $currentFolder "../../"

Write-Host "********* BUILDING DbMigrator *********" -ForegroundColor Green
$dbMigratorFolder = Join-Path $slnFolder "src/AbpSolution2.DbMigrator"
Set-Location $dbMigratorFolder
dotnet publish -c Release
docker build -f Dockerfile.local -t abpsolution2-db-migrator:$version .



Write-Host "********* BUILDING Angular Application *********" -ForegroundColor Green
$angularAppFolder = Join-Path $slnFolder "./angular"
Set-Location $angularAppFolder
npx yarn
npm run build:prod
docker build -f Dockerfile.local -t abpsolution2-angular:$version .

Write-Host "********* BUILDING Api.Host Application *********" -ForegroundColor Green
$hostFolder = Join-Path $slnFolder "src/AbpSolution2.HttpApi.Host"
Set-Location $hostFolder
dotnet publish -c Release
docker build -f Dockerfile.local -t abpsolution2-api:$version .





Write-Host "********* BUILDING AuthServer Application *********" -ForegroundColor Green
$authServerAppFolder = Join-Path $slnFolder "src/AbpSolution2.AuthServer"
Set-Location $authServerAppFolder
dotnet publish -c Release
docker build -f Dockerfile.local -t abpsolution2-authserver:$version .

### ALL COMPLETED
Write-Host "COMPLETED" -ForegroundColor Green
Set-Location $currentFolder
exit $LASTEXITCODE