using AbpSolution2.Localization;
using Volo.Abp.AspNetCore.Mvc;

namespace AbpSolution2.Controllers;

/* Inherit your controllers from this class.
 */
public abstract class AbpSolution2Controller : AbpControllerBase
{
    protected AbpSolution2Controller()
    {
        LocalizationResource = typeof(AbpSolution2Resource);
    }
}
