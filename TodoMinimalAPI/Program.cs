using Microsoft.AspNetCore.Authentication.Cookies;
using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.AspNetCore.Builder;
using Microsoft.EntityFrameworkCore;
using TodoMinimalAPI;
using TodoMinimalAPI.Data;
using TodoMinimalAPI.Models;

var builder = WebApplication.CreateBuilder(args);
// Requires Microsoft.AspNetCore.Authentication.JwtBearer
//builder.Services.AddAuthentication("LocalAuthIssuer").AddJwtBearer();

builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
                .AddJwtBearer(JwtBearerDefaults.AuthenticationScheme, options => builder.Configuration.Bind("LocalAuthIssuer", options))
                .AddCookie(CookieAuthenticationDefaults.AuthenticationScheme, options => builder.Configuration.Bind("CookieSettings", options));

// Create scope and role for authorization
builder.Services.AddAuthorizationBuilder()
            .AddPolicy("admin_greetings", policy => policy
            .RequireRole("admin")
            .RequireClaim("scope", "greetings_api"));
builder.Services.AddAuthorization();

builder.Services.AddDbContext<TodoDbContext>(option => option.UseInMemoryDatabase("TodoList"));
builder.Services.AddDatabaseDeveloperPageExceptionFilter();

//Step 1: First of all, install NSwag => dotnet add package NSwag.AspNetCore

//Step 2: Enables the API Explorer, which is a service that provides metadata about the HTTP API. The API Explorer is used by Swagger to generate the Swagger document.
builder.Services.AddEndpointsApiExplorer();

//Step 3: Adds the Swagger OpenAPI document generator to the application services and configures it to provide more information about the API
builder.Services.AddOpenApiDocument(config =>
{
    config.DocumentName = "TodoAPI";
    config.Title = "TodoAPI v1 - Minimal version";
    config.Version = "v1";
});

var app = builder.Build();
app.Urls.Add("http://localhost:3000");
app.Urls.Add("http://localhost:4000");

if (app.Environment.IsDevelopment())
{
    app.UseOpenApi();
    app.UseSwaggerUi(config =>
    {
        config.DocumentTitle = "TodoAPI";
        config.Path = "/swagger";
        config.DocumentPath = "/swagger/{documentName}/swagger.json";
        config.DocExpansion = "list";
    });
    app.UseDeveloperExceptionPage();
}

app.UseDefaultFiles();
app.UseStaticFiles();

// Endpoint defined outside of Program.cs
TodoEndpoints.Map(app); 

app.Run();