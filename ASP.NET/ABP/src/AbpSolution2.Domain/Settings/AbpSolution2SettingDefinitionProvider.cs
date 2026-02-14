using Volo.Abp.Settings;

namespace AbpSolution2.Settings;

public class AbpSolution2SettingDefinitionProvider : SettingDefinitionProvider
{
    public override void Define(ISettingDefinitionContext context)
    {
        //Define your own settings here. Example:
        //context.Add(new SettingDefinition(AbpSolution2Settings.MySetting1));
    }
}
