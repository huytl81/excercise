using Microsoft.EntityFrameworkCore;

namespace Product.Microservice.Data
{
    public interface IProductDbContext
    {
        DbSet<Models.Product> Products { get; set; }
        Task<int> SaveChanges();

    }
}
