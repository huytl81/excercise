using AbpSolution2.Samples;
using Xunit;

namespace AbpSolution2.EntityFrameworkCore.Domains;

[Collection(AbpSolution2TestConsts.CollectionDefinitionName)]
public class EfCoreSampleDomainTests : SampleDomainTests<AbpSolution2EntityFrameworkCoreTestModule>
{

}
