using AbpSolution2.Samples;
using Xunit;

namespace AbpSolution2.EntityFrameworkCore.Applications;

[Collection(AbpSolution2TestConsts.CollectionDefinitionName)]
public class EfCoreSampleAppServiceTests : SampleAppServiceTests<AbpSolution2EntityFrameworkCoreTestModule>
{

}
