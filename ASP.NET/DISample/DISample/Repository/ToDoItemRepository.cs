using DISample.Models;
using DISample.Service.DTOs;


namespace DISample.Repository
{
    public class ToDoItemRepository : IToDoItemRepository
    {
        private readonly ToDoDbContext _context;
        public ToDoItemRepository(ToDoDbContext context)
        {
            _context = context;
        }
        public List<TodoItem> List()
        {
            return _context.ToDo!.ToList();
        }
    }
}