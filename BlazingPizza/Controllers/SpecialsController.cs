using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using BlazingPizza.Data;

namespace BlazingPizza.Controllers;

[Route("api/[controller]")]
[ApiController]
[Produces("application/json")]
public class SpecialsController : Controller
{
    private readonly PizzaStoreContext _db;

    public SpecialsController(PizzaStoreContext db)
    {
        _db = db;
    }

    [HttpGet]
    public async Task<ActionResult<List<PizzaSpecial>>> OnInitializedAsync()
    {
        var  lstSpecials = await _db.Specials.ToListAsync();
        var lstOrdered =  lstSpecials.OrderByDescending(s => s.BasePrice).ToList();

         return lstOrdered;
    }
    
    // [HttpGet]
    // //public async Task<ActionResult<List<PizzaSpecial>>> GetSpecialsAsync()
    // public async Task<List<PizzaSpecial>> bbbAsync()
    // {
    //     var  lstSpecials = await _db.Specials.ToListAsync();
    //     var lstOrdered =  lstSpecials.OrderByDescending(s => s.BasePrice).ToList();

    //     return lstOrdered;
    // }
}