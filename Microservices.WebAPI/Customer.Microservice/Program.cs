using Customer.Microservice.Data;
using Customer.Microservice.Models;
using Microsoft.EntityFrameworkCore;
using Microsoft.OpenApi.Models;
using Customer.Microservice.Models;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
builder.Services.AddDbContext<CustomerDbContext>(options => 
    options.UseSqlServer(builder.Configuration.GetConnectionString("CustomerDbContext") ?? throw new InvalidOperationException("Connection string 'CustomerDbContext' not found."), b => b.MigrationsAssembly(typeof(CustomerDbContext).Assembly.FullName)));
builder.Services.AddScoped<ICustomerDbContext, CustomerDbContext>();
//builder.Services.AddScoped<ICustomerDbContext>(provider => provider.GetService<CustomerDbContext>());

builder.Services.AddControllers();
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen(options =>
{
    //options.IncludeXmlComments($@"{System.AppDomain.CurrentDomain.BaseDirectory}\Customer.Microservice.xml");
    options.IncludeXmlComments("Customer.Microservice.xml");
    options.SwaggerDoc("v1", new OpenApiInfo
    {
        Version = "v1",
        Title = "Customer Microservice API",
    });
});

var app = builder.Build();

// Seed data
using (var scope = app.Services.CreateScope())
{
    var services = scope.ServiceProvider;

    SeedData.Initialize(services);
}

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI(options =>
    {
        options.SwaggerEndpoint("/swagger/v1/swagger.json", "Customer.Microservice");
    });
}

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

app.Run();
