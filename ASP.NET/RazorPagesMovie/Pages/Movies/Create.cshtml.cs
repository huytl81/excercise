using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Mvc.RazorPages;
using Microsoft.EntityFrameworkCore;
using RazorPagesMovie.Models;

namespace RazorPagesMovie.Pages.Movies
{
    public class CreateModel : PageModel
    {
        private readonly RazorPagesMovie.Data.RazorPagesMovieContext _context;

        public CreateModel(RazorPagesMovie.Data.RazorPagesMovieContext context)
        {
            _context = context;
        }

        [BindProperty]
        public Movie Movie { get; set; } = default!;

        [ViewData]
        public string Title { get; set; } = "Create movie";

        [TempData]
        public string Message { get; set; }

        public IActionResult OnGetAsync()
        {
            return Page();
        }

        // To protect from overposting attacks, see https://aka.ms/RazorPagesCRUD
        public async Task<IActionResult> OnPostAsync()
        {
            if (!ModelState.IsValid)
            {
                return Page();
            }

            //_context.Movie.Add(Movie);

            _context.Attach(Movie).State = EntityState.Added;
            await _context.SaveChangesAsync();

            Message = $"Movie {Movie.Title} has been added!";

            return RedirectToPage("./Index");
        }
    }
}
