using Microsoft.AspNetCore.Mvc;
using ViewsComponent.Models;

namespace ViewsComponent.Controllers;

public class ToDoController : Controller
{
    private readonly ToDoDBContext _ToDoDBContext;

    public ToDoController(ToDoDBContext context)
    {
        _ToDoDBContext = context;

        // EnsureCreated() is used to call OnModelCreating for In-Memory databases as migration is not possible
        // see: https://github.com/aspnet/EntityFrameworkCore/issues/11666 
        _ToDoDBContext.Database.EnsureCreated();
    }

    public IActionResult Index(int maxPriority = 3, bool isDone = true)
    {
        var model = _ToDoDBContext!.ToDo!.ToList();
        ViewData["maxPriority"] = maxPriority;
        ViewData["isDone"] = isDone;
        ViewBag.PriorityMessage = "My PVC view component";

        return View(model);
    }

    public IActionResult IndexVC(int maxPriority = 3, bool isDone = false)
    {
        return ViewComponent("PriorityList",
            new
            {
                maxPriority = maxPriority,
                isDone = isDone
            });
    }
}
