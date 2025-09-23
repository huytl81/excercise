using DISample.Service.DTOs;

namespace DISample.Services
{
    public class BetterProductService : IProductService
    {
        public List<TodoItem> GetAll()
        {
            return new List<TodoItem>
            {
                new TodoItem { Id = 1, Name = "Sen thoi 1" },
                new TodoItem { Id = 2, Name = "Sen thoi 2" },
                new TodoItem { Id = 3, Name = "Sen thoi 3" },
                new TodoItem { Id = 4, Name = "Sen thoi 4" },
                new TodoItem { Id = 5, Name = "Sen thoi 5" },
                new TodoItem { Id = 5, Name = "Sen thoi 6" },
                new TodoItem { Id = 5, Name = "Sen thoi 7" },
                new TodoItem { Id = 5, Name = "Sen thoi 8" },
            };
        }
    }
}
