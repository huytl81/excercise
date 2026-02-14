using Volo.Abp.Modularity;

namespace AbpSolution2;

public abstract class AbpSolution2ApplicationTestBase<TStartupModule> : AbpSolution2TestBase<TStartupModule>
    where TStartupModule : IAbpModule
{

}
