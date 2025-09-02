using Microsoft.EntityFrameworkCore;
using System.Collections.Generic;

namespace Customer.Microservice.Data
{
    public interface ICustomerDbContext
    {
        DbSet<Models.Customer> Customers { get; set; }
        Task<int> SaveChanges();
    }
}
