using Microsoft.EntityFrameworkCore;
using TodoMinimalAPI.Models;

namespace TodoMinimalAPI.Data
{
    public class TodoDbContext : DbContext
    {
        public TodoDbContext(DbContextOptions<TodoDbContext> options) : base(options)
        {
        }
        
        public DbSet<TodoItem> TodoItems => Set<TodoItem>();
    }
}
