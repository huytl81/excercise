using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using ViewsComponent.Models;

namespace ViewsComponent.ViewComponents;

public class PriorityList : ViewComponent
{
    private readonly ToDoContext db;

    public PriorityList(ToDoContext context) => db = context;

    public async Task<IViewComponentResult> InvokeAsync(int maxPriority, bool isDone)
    {
        string viewname = "Default";
        // If asking for all completed tasks, render with the "PVC" view.
        if (maxPriority > 3 && isDone == true)
        {
            viewname = "PVC";
        }
        var items = await GetItemsAsync(maxPriority, isDone);

        return View(viewname, items);
    }

    private Task<List<TodoItem>> GetItemsAsync(int maxPriority, bool isDone)
    {
        return db!.ToDo!.Where(x => x.IsDone == isDone && x.Priority <= maxPriority).ToListAsync();
    }
}