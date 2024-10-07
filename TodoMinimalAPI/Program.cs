using Microsoft.AspNetCore.Authentication.Cookies;
using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.EntityFrameworkCore;
using TodoMinimalAPI;
using TodoMinimalAPI.Data;
using OpenApiContact = NSwag.OpenApiContact;
using OpenApiInfo = NSwag.OpenApiInfo;
using OpenApiLicense = NSwag.OpenApiLicense;

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

builder.Services.AddOpenApiDocument(options => {
    options.PostProcess = document =>
    {
        document.Info = new OpenApiInfo
        {
            Version = "v1",
            Title = "TodoAPI v1 - Minimal version with Redoc",
            Description = "An ASP.NET Core Web API for managing ToDo items",
            TermsOfService = "https://example.com/terms",
            Contact = new OpenApiContact
            {
                Name = "Example Contact",
                Url = "https://example.com/contact"
            },
            License = new OpenApiLicense
            {
                Name = "Example License",
                Url = "https://example.com/license"
            }
        };
    };
});


var app = builder.Build();
app.Urls.Add("http://localhost:3000");
app.Urls.Add("http://localhost:4000");

if (app.Environment.IsDevelopment())
{
    app.UseOpenApi();
    //ReDoc is exposed via/api-docs we can change this when enabling middleware by setting RoutePrefix:
    //app.UseReDoc(options =>
    //{
    //    options.Path = "/redoc";
    //});
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