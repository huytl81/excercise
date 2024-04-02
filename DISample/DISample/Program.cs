using DISample;
using DISample.Service;

var builder = WebApplication.CreateBuilder(args);

if (builder.Environment.IsDevelopment())
{
    builder.Services.AddTransient<IProductService, BetterProductService>();
}
else
{
    builder.Services.AddTransient<IProductService, ProductService>();
}

// Add services to the container.
builder.Services.AddControllersWithViews();

//builder.Services.AddTransient<ITransientService, SomeService>().AddScoped<IScopedService, SomeService>().AddSingleton<ISingletonService, SomeService>();
//builder.Services.AddScoped<IScopedService, SomeService>();
//builder.Services.AddSingleton<ISingletonService, SomeService>();

builder.Services.AddMyConfigCollection(builder.Configuration).AddMyServiceCollection();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}");

app.Run();
