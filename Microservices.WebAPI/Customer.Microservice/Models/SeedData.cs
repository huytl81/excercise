using Customer.Microservice.Data;
using Microsoft.EntityFrameworkCore;

namespace Customer.Microservice.Models;

public static class SeedData
{
    
    public static async void Initialize(IServiceProvider serviceProvider)
    {
        using (var context = new CustomerDbContext(serviceProvider.GetRequiredService<DbContextOptions<CustomerDbContext>>()))
        {
            // Look for any movies.
            if (context.Customers.Any())
            {
                return;   // DB has been seeded
            }
            context.Customers.AddRange(
                new Customer
                {
                    Name = "Huy Ta",
                    Email = "huyta@gmail.com",
                    City = "Romantic Capital",
                    Contact = "0982824818"
                },
                new Customer
                {
                    Name = "Harry Sally",
                    Email = "hasa@gmail.com",
                    City = "Ha Noi Capital",
                    Contact = "0982824818"
                },
                new Customer
                {
                    Name = "Sen Thoi",
                    Email = "tadinhtrunghieu@gmail.com",
                    City = "TP. Ho Chi Minh",
                    Contact = "0982824818"
                },
                new Customer
                {
                    Name = "Dao Thanh Ha",
                    Email = "hadao@gmail.com",
                    City = "Ha Noi, Viet Nam",
                    Contact = "0984313978"
                }
            );
            await context.SaveChanges();
        }
    }
}
