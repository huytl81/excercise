using Microsoft.Extensions.Localization;
using AbpSolution2.Localization;
using Volo.Abp.DependencyInjection;
using Volo.Abp.Ui.Branding;

namespace AbpSolution2;

[Dependency(ReplaceServices = true)]
public class AbpSolution2BrandingProvider : DefaultBrandingProvider
{
    private IStringLocalizer<AbpSolution2Resource> _localizer;

    public AbpSolution2BrandingProvider(IStringLocalizer<AbpSolution2Resource> localizer)
    {
        _localizer = localizer;
    }

    public override string AppName => _localizer["AppName"];
}
