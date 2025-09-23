namespace Product.Microservice.Repository
{
    public interface IProductRepository
    {
        Task<IEnumerable<Models.Product>> GetProducts();
        Task<Models.Product> GetProductByID(int productId);
        Task InsertProduct(Models.Product product);
        Task UpdateProduct(Models.Product product);
        Task DeleteProduct(int productId);
        Task Save();
    }
}
