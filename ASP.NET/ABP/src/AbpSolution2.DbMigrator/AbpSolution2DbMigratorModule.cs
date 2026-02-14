using AbpSolution2.EntityFrameworkCore;
using Volo.Abp.Autofac;
using Volo.Abp.Caching;
using Volo.Abp.Caching.StackExchangeRedis;
using Microsoft.Extensions.DependencyInjection;
using Volo.Abp.Modularity;

namespace AbpSolution2.DbMigrator;

[DependsOn(
    typeof(AbpAutofacModule),
    typeof(AbpCachingStackExchangeRedisModule),
    typeof(AbpSolution2EntityFrameworkCoreModule),
    typeof(AbpSolution2ApplicationContractsModule)
)]
public class AbpSolution2DbMigratorModule : AbpModule
{
    public override void PreConfigureServices(ServiceConfigurationContext context)
    {
        if (Program.DisableRedis)
        {
            var configuration = context.Services.GetConfiguration();
            configuration["Redis:IsEnabled"] = "false";
        }
        
        base.PreConfigureServices(context);
    }

    public override void ConfigureServices(ServiceConfigurationContext context)
    {
        Configure<AbpDistributedCacheOptions>(options => { options.KeyPrefix = "AbpSolution2:"; });
    }
}
