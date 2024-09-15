using Humanizer;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.OpenApi.Models;
using System.Reflection;
using TodoControllerAPI.Data;
[assembly: ApiController]

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.

builder.Services.AddControllers()
                .ConfigureApiBehaviorOptions(options =>
                {
                    // To preserve the default behavior, capture the original delegate to call later.
                    var builtInFactory = options.InvalidModelStateResponseFactory;
                    // retrieve an instance of ILogger<TCategoryName> to log information about an automatic 400 response
                    options.InvalidModelStateResponseFactory = context =>
                    {
                        var logger = context.HttpContext.RequestServices.GetRequiredService<ILogger<Program>>();

                        // Perform logging here.
                        // ...

                        // Invoke the default behavior, which produces a ValidationProblemDetails
                        // response.
                        // To produce a custom response, return a different implementation of 
                        // IActionResult instead.
                        return builtInFactory(context);
                    };
                    //disable the action parameters of type IFormFile and IFormFileCollection
                    //options.SuppressConsumesConstraintForFormFileParameters = true;
                    
                    //Disable binding source inference, set SuppressInferBindingSourcesForParameters to true
                    //options.SuppressInferBindingSourcesForParameters = true;

                    //Disable automatic 400 response
                    //options.SuppressModelStateInvalidFilter = true;
                    
                    //Disable ProblemDetails response
                    //options.SuppressMapClientErrors = true;
                    options.ClientErrorMapping[StatusCodes.Status404NotFound].Link = "https://httpstatuses.com/404";

                    //Disable[FromServices] inference globally, set DisableImplicitFromServicesParameters to true
                    //options.DisableImplicitFromServicesParameters = true;
                });
builder.Services.AddDbContext<TodoContext>(option => option.UseInMemoryDatabase("TodoList"));
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen(options =>
{
    options.SwaggerDoc("v1", new OpenApiInfo
    {
        Version = "v1",
        Title = "ToDo API",
        Description = "An ASP.NET Core Web API for managing ToDo items",
        TermsOfService = new Uri("https://example.com/terms"),
        Contact = new OpenApiContact
        {
            Name = "Example Contact",
            Url = new Uri("https://example.com/contact")
        },
        License = new OpenApiLicense
        {
            Name = "Example License",
            Url = new Uri("https://example.com/license")
        }
    });
    // using System.Reflection;
    var xmlFilename = $"{Assembly.GetExecutingAssembly().GetName().Name}.xml";
    options.IncludeXmlComments(Path.Combine(AppContext.BaseDirectory, xmlFilename));
});

builder.Services.AddKeyedSingleton<ICache, BigCache>("big");
builder.Services.AddKeyedSingleton<ICache, SmallCache>("small");

var app = builder.Build();

app.MapGet("/big", ([FromKeyedServices("big")] ICache bigCache) => bigCache.Get("date"));
app.MapGet("/small", ([FromKeyedServices("small")] ICache smallCache) => smallCache.Get("date"));

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    //app.UseSwagger(options =>
    //{
    //    options.SerializeAsV2 = true;
    //});
    app.UseSwagger();
    app.UseSwaggerUI(options =>
    {
        options.SwaggerEndpoint("/swagger/v1/swagger.json", "v1");
        options.RoutePrefix = string.Empty;
        options.InjectStylesheet("/swagger-ui/custom.css");
    });
}

app.UseHttpsRedirection();

app.UseStaticFiles();

app.UseAuthorization();

app.MapControllers();

app.Run();

public interface ICache
{
    object Get(string key);
}
public class BigCache : ICache
{
    public object Get(string key) => $"Resolving {key} from big cache.";
}

public class SmallCache : ICache
{
    public object Get(string key) => $"Resolving {key} from small cache.";
}