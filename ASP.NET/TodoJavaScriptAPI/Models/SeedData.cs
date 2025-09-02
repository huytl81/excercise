using Microsoft.EntityFrameworkCore;
using TodoJavaScriptAPI.Data;

namespace TodoJavaScriptAPI.Models;

public static class SeedData
{
    public static void Initialize(IServiceProvider serviceProvider)
    {
        using (var context = new TodoContext(serviceProvider.GetRequiredService<DbContextOptions<TodoContext>>()))
        {
            // Look for any movies.
            if (context.TodoItems.Any())
            {
                return;   // DB has been seeded
            }
            context.TodoItems.AddRange(
                new TodoItem
                {
                    Name = "When Harry Met Sally",
                    IsComplete = false
                }
            );
            context.SaveChanges();
        }
    }
}