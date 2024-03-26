using DISample.Models;
using Microsoft.AspNetCore.Mvc;
using System.Diagnostics;
using DISample.Service;
using DISample.Services;

namespace DISample.Controllers
{
    public class HomeController : Controller
    {
        private readonly ILogger<HomeController> _logger;
        private readonly IProductService _productService;

        private readonly ITransientService _iTransientService1;
        private readonly ITransientService _iTransientService2;

        private readonly IScopedService _iScopedService1;
        private readonly IScopedService _iScopedService2;

        private readonly ISingletonService _iSingletonService1;
        private readonly ISingletonService _iSingletonService2;

        public HomeController(ILogger<HomeController> logger, 
            IProductService productService, 

            ITransientService iTransientService1, 
            ITransientService iTransientService2,

            IScopedService iScopedService1,
            IScopedService iScopedService2,

            ISingletonService iSingletonService1,
            ISingletonService iSingletonService2
            )
        {
            //_productService = new ProductService();
            _productService = productService;

            _iTransientService1 = iTransientService1;
            _iTransientService2 = iTransientService2;

            _iScopedService1 = iScopedService1;
            _iScopedService2 = iScopedService2;

            _iSingletonService1 = iSingletonService1;
            _iSingletonService2 = iSingletonService2;

            _logger = logger;
        }

        public IActionResult Index()
        {
            var lstProducts = _productService.GetAll();

            ViewBag.Message1 = "First Instance: " + _iTransientService1.GetGuid().ToString();
            ViewBag.Message2 = "Second Instance: " + _iTransientService2.GetGuid().ToString();

            ViewBag.Message3 = "First Instance: " + _iScopedService1.GetGuid().ToString();
            ViewBag.Message4 = "Second Instance: " + _iScopedService2.GetGuid().ToString();

            ViewBag.Message5 = "First Instance: " + _iSingletonService1.GetGuid().ToString();
            ViewBag.Message6 = "Second Instance: " + _iSingletonService1.GetGuid().ToString();

            return View(lstProducts);
        }

        //private readonly ILogger<HomeController> _logger;

        //public HomeController(ILogger<HomeController> logger)
        //{
        //    _logger = logger;
        //}

        //public IActionResult Index([FromServices] IProductService productService)
        //{
        //    var lstProducts = productService.GetAll();
        //    return View(lstProducts);
        //}


        public IActionResult Privacy()
        {
            return View();
        }

        [ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
        public IActionResult Error()
        {
            return View(new ErrorViewModel { RequestId = Activity.Current?.Id ?? HttpContext.TraceIdentifier });
        }
    }
}
