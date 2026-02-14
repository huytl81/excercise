./build-image.ps1 -ProjectPath "../../src/AbpSolution2.DbMigrator/AbpSolution2.DbMigrator.csproj" -ImageName abpsolution2/dbmigrator
./build-image.ps1 -ProjectPath "../../src/AbpSolution2.HttpApi.Host/AbpSolution2.HttpApi.Host.csproj" -ImageName abpsolution2/httpapihost
./build-image.ps1 -ProjectPath "../../angular" -ImageName abpsolution2/angular -ProjectType "angular"
./build-image.ps1 -ProjectPath "../../src/AbpSolution2.AuthServer/AbpSolution2.AuthServer.csproj" -ImageName abpsolution2/authserver
