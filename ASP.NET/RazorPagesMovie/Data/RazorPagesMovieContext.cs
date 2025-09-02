using Microsoft.EntityFrameworkCore;
using RazorPagesMovie.Models;

namespace RazorPagesMovie.Data
{
    public class RazorPagesMovieContext(DbContextOptions<RazorPagesMovieContext> options) : DbContext(options)
    {
        //public RazorPagesMovieContext (DbContextOptions<RazorPagesMovieContext> options) : base(options) { }

        public DbSet<Movie> Movie { get; set; } = default!;
    }
}
