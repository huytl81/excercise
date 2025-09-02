using Product.Microservice.Data;
using Microsoft.EntityFrameworkCore;

namespace Product.Microservice.Models;

public static class SeedData
{
    
    public static async void Initialize(IServiceProvider serviceProvider)
    {
        await using var context = new ProductDbContext(serviceProvider.GetRequiredService<DbContextOptions<ProductDbContext>>());
        // Look for any movies.
        if (context.Products.Any())
        {
            return;   // DB has been seeded
        }
        context.Products.AddRange(
            new Product
            {
                Name = "Egg",
                Description = "Chicken egg",
                Price = 6.99,
                Quantity = 1700
            },
            new Product
            {
                Name = "Beef",
                Description = "Beef, cow's meat",
                Price = 66.99,
                Quantity = 45
            },
            new Product
            {
                Name = "Chicken",
                Description = "Chicken meat",
                Price = 16.99,
                Quantity = 100
            },
            new Product
            {
                Name = "Goose",
                Description = "Geese meat",
                Price = 16.99,
                Quantity = 58
            }
        );

        await context.SaveChanges();
    }
}
