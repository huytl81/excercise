using Microsoft.EntityFrameworkCore;
using TodoJavaScriptAPI.Models;

namespace TodoJavaScriptAPI.Data
{
    public class TodoContext : DbContext
    {
        public TodoContext(DbContextOptions<TodoContext> options) : base(options)
        {
        }

        public DbSet<TodoItem> TodoItems => Set<TodoItem>();
    }
}
