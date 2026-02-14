using System;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.DependencyInjection;
using AbpSolution2.Data;
using Volo.Abp.DependencyInjection;

namespace AbpSolution2.EntityFrameworkCore;

public class EntityFrameworkCoreAbpSolution2DbSchemaMigrator
    : IAbpSolution2DbSchemaMigrator, ITransientDependency
{
    private readonly IServiceProvider _serviceProvider;

    public EntityFrameworkCoreAbpSolution2DbSchemaMigrator(IServiceProvider serviceProvider)
    {
        _serviceProvider = serviceProvider;
    }

    public async Task MigrateAsync()
    {
        /* We intentionally resolving the AbpSolution2DbContext
         * from IServiceProvider (instead of directly injecting it)
         * to properly get the connection string of the current tenant in the
         * current scope.
         */

        await _serviceProvider
            .GetRequiredService<AbpSolution2DbContext>()
            .Database
            .MigrateAsync();
    }
}
