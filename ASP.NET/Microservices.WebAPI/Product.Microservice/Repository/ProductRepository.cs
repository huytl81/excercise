using Microsoft.EntityFrameworkCore;
using Product.Microservice.Data;
using System.Collections.Generic;
using System.Threading.Tasks;

namespace Product.Microservice.Repository
{
    public class ProductRepository : IProductRepository
    {
        private readonly ProductDbContext _dbContext;

        public ProductRepository(ProductDbContext dbContext)
        {
            _dbContext = dbContext;
        }
        public async Task DeleteProduct(int productId)
        {
            var product = _dbContext.Products.Find(productId);
            _dbContext.Products.Remove(product);
            await Save();
        }

        public async Task<Models.Product> GetProductByID(int productId)
        {
            return await _dbContext.Products.FindAsync(productId);
        }

        public async Task<List<Models.Product>> GetProducts()
        {
            return await _dbContext.Products.ToListAsync();
        }

        public async Task InsertProduct(Models.Product product)
        {
            _dbContext.Add(product);
            await Save();
        }

        public async Task UpdateProduct(Models.Product product)
        {
            _dbContext.Entry(product).State = EntityState.Modified;
            await Save();
        }

        public async Task Save()
        {
            await _dbContext.SaveChangesAsync();
        }

        
    }
}