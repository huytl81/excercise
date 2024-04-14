using Microsoft.AspNetCore.Mvc;
using MVCMovie.Models;
using System.Diagnostics;

namespace MVCMovie.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;

        public HomeController(ILogger<HomeController> logger)
        {
            _logger = logger;
        }

        [ViewData]
        public string Hello { get; set; }

        [TempData]
        public string MyTemp { get; set; }

        public IActionResult Index()
        {
            
            Hello = "ViewData attribute!";
            ViewData["Body"] = "ViewData";
            ViewBag.Message = "ViewBag";

            return View();
        }

        public IActionResult Privacy()
        {
            MyTemp = "Where is this?";

            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
