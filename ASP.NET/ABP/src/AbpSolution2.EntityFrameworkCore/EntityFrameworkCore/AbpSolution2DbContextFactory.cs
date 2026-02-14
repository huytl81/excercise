using System;
using System.IO;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Design;
using Microsoft.Extensions.Configuration;

namespace AbpSolution2.EntityFrameworkCore;

/* This class is needed for EF Core console commands
 * (like Add-Migration and Update-Database commands) */
public class AbpSolution2DbContextFactory : IDesignTimeDbContextFactory<AbpSolution2DbContext>
{
    public AbpSolution2DbContext CreateDbContext(string[] args)
    {
        // https://www.npgsql.org/efcore/release-notes/6.0.html#opting-out-of-the-new-timestamp-mapping-logic
        AppContext.SetSwitch("Npgsql.EnableLegacyTimestampBehavior", true);
        
        var configuration = BuildConfiguration();
        
        AbpSolution2EfCoreEntityExtensionMappings.Configure();

        var builder = new DbContextOptionsBuilder<AbpSolution2DbContext>()
            .UseNpgsql(configuration.GetConnectionString("Default"));
        
        return new AbpSolution2DbContext(builder.Options);
    }

    private static IConfigurationRoot BuildConfiguration()
    {
        var builder = new ConfigurationBuilder()
            .SetBasePath(Path.Combine(Directory.GetCurrentDirectory(), "../AbpSolution2.DbMigrator/"))
            .AddJsonFile("appsettings.json", optional: false)
            .AddEnvironmentVariables();

        return builder.Build();
    }
}
