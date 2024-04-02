using Customer.Microservice.Data;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace Customer.Microservice.Controllers
{
    [Route("api/[controller]")]
    [ApiController]
    public class CustomerController : ControllerBase
    {
        private readonly ICustomerDbContext _context;
        public CustomerController(ICustomerDbContext context)
        {
            _context = context;
        }

        [HttpGet]
        public async Task<IActionResult> GetCustomers()
        {
            var customers = await _context.Customers.ToListAsync();

            return Ok(customers);
        }

        [HttpGet("{id}")]
        public async Task<IActionResult> GetCustomerById(int id)
        {
            var customer = await _context.Customers.Where(x => x.Id == id).FirstOrDefaultAsync();
            if (customer == null) return NotFound();

            return Ok(customer);
        }

        [HttpPost]
        public async Task<IActionResult> Create(Models.Customer customer)
        {
            _context.Customers.Add(customer);
            await _context.SaveChanges();

            return Ok(customer.Id);
        }

        [HttpPut("{id}")]
        public async Task<IActionResult> Update(int id, Models.Customer customerData)
        {
            var customer = _context.Customers.Where(a => a.Id == id).FirstOrDefault();

            if (customer == null)
            {
                return NotFound();
            }

            customer.City = customerData.City;
            customer.Name = customerData.Name;
            customer.Contact = customerData.Contact;
            customer.Email = customerData.Email;

            await _context.SaveChanges();

            return Ok(customer.Id);
        }

        [HttpDelete("{id}")]
        public async Task<IActionResult> Delete(int id)
        {
            var customer = await _context.Customers.Where(a => a.Id == id).FirstOrDefaultAsync();
            if (customer == null) return NotFound();
            _context.Customers.Remove(customer);
            await _context.SaveChanges();

            return Ok(customer.Id);
        }
    }
}