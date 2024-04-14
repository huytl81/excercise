using Microsoft.AspNetCore.Mvc;
using ViewsComponent.Models;

namespace ViewsComponent.Controllers;

public class ToDoController : Controller
{
    private readonly ToDoContext _ToDoContext;

    public ToDoController(ToDoContext context)
    {
        _ToDoContext = context;

        // EnsureCreated() is used to call OnModelCreating for In-Memory databases as migration is not possible
        // see: https://github.com/aspnet/EntityFrameworkCore/issues/11666 
        _ToDoContext.Database.EnsureCreated();
    }

    public IActionResult Index(int maxPriority = 4, bool isDone = true)
    {
        var model = _ToDoContext!.ToDo!.ToList();
        ViewData["maxPriority"] = maxPriority;
        ViewData["isDone"] = isDone;

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
