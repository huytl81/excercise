using DISample.Services;

namespace DISample
{
    public static class MyConfigServiceCollectionExtensions
    {
        //public static IConfiguration AddMyConfigCollection(this IConfiguration configuration, IServiceCollection services)
        //{
        //    services.Configure<PositionOptions>(configuration.GetSection(PositionOptions.Position));
        //    services.Configure<ColorOptions>(configuration.GetSection(ColorOptions.Color));

        //    return configuration;
        //}

        public static IServiceCollection AddMyServiceCollection(this IServiceCollection services)
        {
            services.AddTransient<ITransientService, GuidService>();
            services.AddScoped<IScopedService, GuidService>();
            services.AddSingleton<ISingletonService, GuidService>();

            return services;
        }
    }
}
