using System.Threading.Tasks;

namespace AbpSolution2.Data;

public interface IAbpSolution2DbSchemaMigrator
{
    Task MigrateAsync();
}
