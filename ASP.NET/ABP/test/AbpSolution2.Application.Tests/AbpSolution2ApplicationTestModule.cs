using Volo.Abp.Modularity;

namespace AbpSolution2;

[DependsOn(
    typeof(AbpSolution2ApplicationModule),
    typeof(AbpSolution2DomainTestModule)
)]
public class AbpSolution2ApplicationTestModule : AbpModule
{

}
