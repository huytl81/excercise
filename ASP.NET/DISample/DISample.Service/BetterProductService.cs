using DISample.Service.DTOs;

namespace DISample.Service
{
    public class BetterProductService : IProductService
    {
        public List<ProductViewModel> GetAll()
        {
            return new List<ProductViewModel>
            {
                new ProductViewModel { Id = 1, Name = "Sen thoi 1" },
                new ProductViewModel { Id = 2, Name = "Sen thoi 2" },
                new ProductViewModel { Id = 3, Name = "Sen thoi 3" },
                new ProductViewModel { Id = 4, Name = "Sen thoi 4" },
                new ProductViewModel { Id = 5, Name = "Sen thoi 5" },
                new ProductViewModel { Id = 5, Name = "Sen thoi 6" },
                new ProductViewModel { Id = 5, Name = "Sen thoi 7" },
                new ProductViewModel { Id = 5, Name = "Sen thoi 8" },
            };
        }
    }
}
