using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.EntityFrameworkCore;
using MvcMovie.Models;

namespace MVCMovie.Data
{
    public class MvcMovieContext(DbContextOptions<MvcMovieContext> options) : DbContext(options)
    {
        
        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder
                .UseLazyLoadingProxies();
        }

        public DbSet<MvcMovie.Models.Movie> Movie { get; set; } = default!;
    }
}
