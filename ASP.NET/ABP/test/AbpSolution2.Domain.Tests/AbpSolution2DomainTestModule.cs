using Volo.Abp.Modularity;

namespace AbpSolution2;

[DependsOn(
    typeof(AbpSolution2DomainModule),
    typeof(AbpSolution2TestBaseModule)
)]
public class AbpSolution2DomainTestModule : AbpModule
{

}
