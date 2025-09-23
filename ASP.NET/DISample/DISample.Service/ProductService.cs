using DISample.Service.DTOs;

namespace DISample.Services
{
    public class ProductService : IProductService
    {
        public List<TodoItem> GetAll()
        {
            return new List<TodoItem>
            {
                new TodoItem { Id = 1, Name = "Huy Ta 1" },
                new TodoItem { Id = 2, Name = "Huy Ta 2" },
                new TodoItem { Id = 3, Name = "Huy Ta 3" }
            };
        }
    }
}
