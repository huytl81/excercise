using Microsoft.EntityFrameworkCore;
using ViewsComponent.Models;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddDbContext<ToDoDbContext>(options => options.UseInMemoryDatabase("db"));

builder.Services.AddControllersWithViews().AddRazorOptions(options =>
{
    options.ViewLocationFormats.Add("/{0}.cshtml");
});

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Home/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Todo}/{action=Index}/{id?}");

app.Run();
