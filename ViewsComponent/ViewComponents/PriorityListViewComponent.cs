using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using ViewsComponent.Models;

namespace ViewsComponent.ViewComponents;

//[ViewComponent(Name = "PriorityList")]
//public class PriorityListViewComponent : ViewComponent
public class PriorityList : ViewComponent
{
    private readonly ToDoDbContext db;

    public PriorityList(ToDoDbContext context) => db = context;

    public async Task<IViewComponentResult> InvokeAsync(int maxPriority, bool isDone)
    {
        string viewname = "Default";
        // If asking for all completed tasks, render with the "PVC" view.
        if (maxPriority > 2 && isDone)
        {
            viewname = "PVC";
        }
        var items = await GetItemsAsync(maxPriority, isDone);

        return View(viewname, items);
    }

    private  Task<List<TodoItem>> GetItemsAsync(int maxPriority, bool isDone)
    {
        return db!.ToDo!.Where(x => x.IsDone == isDone && x.Priority <= maxPriority).ToListAsync();
    }
}