using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.DependencyInjection;
using MvcMovie.Models;
using MVCMovie.Data;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddControllersWithViews();

if (builder.Environment.IsDevelopment())
{
    //builder.Services.AddDbContext<MvcMovieContext>(options => options.UseSqlite(builder.Configuration.GetConnectionString("MvcMovieContext")));
    builder.Services.AddDbContext<MvcMovieContext>(options => options.UseSqlite(builder.Configuration.GetConnectionString("DevelopmentMvcMovieContext") ?? throw new InvalidOperationException("Connection string 'MvcMovieContext' not found.")));
}
else
{
    //builder.Services.AddDbContext<MvcMovieContext>(options => options.UseSqlServer(builder.Configuration.GetConnectionString("ProductionMvcMovieContext")));
    builder.Services.AddDbContext<MvcMovieContext>(options => options.UseSqlServer(builder.Configuration.GetConnectionString("ProductionMvcMovieContext") ?? throw new InvalidOperationException("Connection string 'ProductionMvcMovieContext' not found.")));
}


var app = builder.Build();

using (var scope = app.Services.CreateScope())
{
    var services = scope.ServiceProvider;

    SeedData.Initialize(services);
}

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
