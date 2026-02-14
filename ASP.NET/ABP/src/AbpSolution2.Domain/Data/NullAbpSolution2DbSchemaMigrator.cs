using System.Threading.Tasks;
using Volo.Abp.DependencyInjection;

namespace AbpSolution2.Data;

/* This is used if database provider does't define
 * IAbpSolution2DbSchemaMigrator implementation.
 */
public class NullAbpSolution2DbSchemaMigrator : IAbpSolution2DbSchemaMigrator, ITransientDependency
{
    public Task MigrateAsync()
    {
        return Task.CompletedTask;
    }
}
