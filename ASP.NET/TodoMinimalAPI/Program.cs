using Microsoft.AspNetCore.Authentication.Cookies;
using Microsoft.AspNetCore.Authentication.JwtBearer;
using Microsoft.EntityFrameworkCore;
using Microsoft.IdentityModel.Tokens;
using System.Text;
using TodoMinimalAPI;
using TodoMinimalAPI.Data;
using OpenApiContact = NSwag.OpenApiContact;
using OpenApiInfo = NSwag.OpenApiInfo;
using OpenApiLicense = NSwag.OpenApiLicense;

var builder = WebApplication.CreateBuilder(args);

// ===== 1. Cấu hình Authentication JWT =====
builder.Services.Configure<JwtSettings>(builder.Configuration.GetSection("Jwt"));
var jwtSettings = builder.Configuration.GetSection("Jwt").Get<JwtSettings>();

var key = builder.Configuration["Jwt:Key"];

builder.Services.AddAuthentication(options =>
{
    options.DefaultAuthenticateScheme = JwtBearerDefaults.AuthenticationScheme;
    options.DefaultChallengeScheme = JwtBearerDefaults.AuthenticationScheme;
}).AddJwtBearer(JwtBearerDefaults.AuthenticationScheme, options =>
{
    options.TokenValidationParameters = new TokenValidationParameters
    {
        ValidateIssuer = false,
        ValidateAudience = false,
        ValidateIssuerSigningKey = true,
        IssuerSigningKey = new SymmetricSecurityKey(Encoding.UTF8.GetBytes(key!)),
        ClockSkew = TimeSpan.Zero
    };
}).AddCookie(CookieAuthenticationDefaults.AuthenticationScheme, options => builder.Configuration.Bind("CookieSettings", options));

// ===== 2. Cấu hình Authorization Policy =====
builder.Services.AddAuthorization(options =>
{
    options.AddPolicy("admin_policy", 
    policy => policy.RequireClaim("scope", "admin_scope").RequireRole("admin_role"));
});


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

app.Urls.Add("https://localhost:7141");
app.Urls.Add("http://localhost:5143");


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

app.UseAuthentication();
app.UseAuthorization();

// Endpoint defined outside of Program.cs
TodoEndpoints.Map(app); 

app.Run();