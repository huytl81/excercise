using DISample.Service.DTOs;

namespace DISample.Service
{
    public class ProductService : IProductService
    {
        public List<ProductViewModel> GetAll()
        {
            return new List<ProductViewModel>
            {
                new ProductViewModel { Id = 1, Name = "Huy Ta 1" },
                new ProductViewModel { Id = 2, Name = "Huy Ta 2" },
                new ProductViewModel { Id = 3, Name = "Huy Ta 3" }
            };
        }
    }
}
