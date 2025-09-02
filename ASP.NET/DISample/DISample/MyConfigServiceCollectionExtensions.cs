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
            services.AddTransient<ITransientService, SomeService>();
            services.AddScoped<IScopedService, SomeService>();
            services.AddSingleton<ISingletonService, SomeService>();

            return services;
        }
    }
}
