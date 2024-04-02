using DISample.Services;

namespace DISample
{
    public static class MyConfigServiceCollectionExtensions
    {
        public static IServiceCollection AddMyConfigCollection(this IServiceCollection services, IConfiguration config)
        {
            //services.Configure<PositionOptions>(config.GetSection(PositionOptions.Position));
            //services.Configure<ColorOptions>(config.GetSection(ColorOptions.Color));

            return services;
        }

        public static IServiceCollection AddMyServiceCollection(this IServiceCollection services)
        {
            services.AddTransient<ITransientService, SomeService>();
            services.AddScoped<IScopedService, SomeService>();
            services.AddSingleton<ISingletonService, SomeService>();

            return services;
        }
    }
}
