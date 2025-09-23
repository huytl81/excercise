using Microsoft.OpenApi.Models;
using Ocelot.DependencyInjection;
using Ocelot.Middleware;



var builder = WebApplication.CreateBuilder(args);
builder.Configuration.AddJsonFile("ocelot.json", optional: false, reloadOnChange: true);
builder.Services.AddOcelot();

builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen(options =>
{
    //options.IncludeXmlComments($@"{System.AppDomain.CurrentDomain.BaseDirectory}\Customer.Microservice.xml");
    options.IncludeXmlComments("GatewayAPI.Microservice.xml");
    options.SwaggerDoc("v1", new OpenApiInfo
    {
        Version = "v1",
        Title = "GatewayAPI Microservice API",
    });
});

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI(options =>
    {
        options.SwaggerEndpoint("/swagger/v1/swagger.json", "Gateway.API");
    });
}


await app.UseOcelot();

app.Run();
