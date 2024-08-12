using Microsoft.AspNetCore.Mvc;
using ViewsComponent.Models;

namespace ViewsComponent.Controllers;

public class ToDoController : Controller
{
    private readonly ToDoDbContext _toDoDbContext;

    public ToDoController(ToDoDbContext context)
    {
        _toDoDbContext = context;

        // EnsureCreated() is used to call OnModelCreating for In-Memory databases as migration is not possible
        // see: https://github.com/aspnet/EntityFrameworkCore/issues/11666 
        _toDoDbContext.Database.EnsureCreated();
    }

    public IActionResult Index(int maxPriority = 2, bool isDone = false)
    {
        var model = _toDoDbContext!.ToDo!.ToList();
        ViewData["maxPriority"] = maxPriority;
        ViewData["isDone"] = isDone;
        ViewBag.PriorityMessage = "My PVC view component";

        return View(model);
    }

    public IActionResult IndexVC(int maxPriority = 9, bool isDone = true)
    {
        return ViewComponent("PriorityList",
            new
            {
                maxPriority = maxPriority,
                isDone = isDone
            });
    }
}
