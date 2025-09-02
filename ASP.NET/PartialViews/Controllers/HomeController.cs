using Microsoft.AspNetCore.Mvc;

namespace PartialViews.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Discovery() => View();

        public IActionResult Error() => View();
    }
}
