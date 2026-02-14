using AbpSolution2.Localization;
using Volo.Abp.Application.Services;

namespace AbpSolution2;

/* Inherit your application services from this class.
 */
public abstract class AbpSolution2AppService : ApplicationService
{
    protected AbpSolution2AppService()
    {
        LocalizationResource = typeof(AbpSolution2Resource);
    }
}
