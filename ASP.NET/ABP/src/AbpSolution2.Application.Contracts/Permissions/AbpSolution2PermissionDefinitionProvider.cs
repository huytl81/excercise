using AbpSolution2.Localization;
using Volo.Abp.Authorization.Permissions;
using Volo.Abp.Localization;
using Volo.Abp.MultiTenancy;

namespace AbpSolution2.Permissions;

public class AbpSolution2PermissionDefinitionProvider : PermissionDefinitionProvider
{
    public override void Define(IPermissionDefinitionContext context)
    {
        var myGroup = context.AddGroup(AbpSolution2Permissions.GroupName);

        myGroup.AddPermission(AbpSolution2Permissions.Dashboard.Host, L("Permission:Dashboard"), MultiTenancySides.Host);
        myGroup.AddPermission(AbpSolution2Permissions.Dashboard.Tenant, L("Permission:Dashboard"), MultiTenancySides.Tenant);

        //Define your own permissions here. Example:
        //myGroup.AddPermission(AbpSolution2Permissions.MyPermission1, L("Permission:MyPermission1"));
    }

    private static LocalizableString L(string name)
    {
        return LocalizableString.Create<AbpSolution2Resource>(name);
    }
}
