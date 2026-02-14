using Volo.Abp.Modularity;

namespace AbpSolution2;

/* Inherit from this class for your domain layer tests. */
public abstract class AbpSolution2DomainTestBase<TStartupModule> : AbpSolution2TestBase<TStartupModule>
    where TStartupModule : IAbpModule
{

}
