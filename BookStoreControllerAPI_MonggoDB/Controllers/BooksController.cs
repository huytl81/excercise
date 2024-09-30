using BookStoreControllerAPI_MonggoDB.Services;
using BookStoreControllerAPI_MonggoDB.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.JsonPatch;
using Microsoft.AspNetCore.Mvc.ModelBinding;


namespace BookStoreControllerAPI_MonggoDB.Controllers;

[ApiController]
[Route("api/[controller]")]
public class BooksController : ControllerBase
{
    private readonly BooksService _booksService;

    public BooksController(BooksService booksService) => _booksService = booksService;

    [HttpGet]
    public async Task<ActionResult<List<Book>>> Gets() => await _booksService.GetAsync();

    [HttpGet("{id:length(24)}")]
    public async Task<ActionResult<Book>> Get(string id)
    {
        var book = await _booksService.GetAsync(id);

        if (book is null)
        {
            return NotFound();
        }

        return book;
    }

    [HttpPost]
    public async Task<IActionResult> Post(Book newBook)
    {
        await _booksService.CreateAsync(newBook);

        return CreatedAtAction(nameof(Get), new { id = newBook.Id }, newBook);
    }

    [HttpPut("{id:length(24)}")]
    public async Task<IActionResult> Put(string id, Book updatedBook)
    {
        var book = await _booksService.GetAsync(id);

        if (book is null)
        {
            return NotFound();
        }

        updatedBook.Id = book.Id;

        await _booksService.UpdateAsync(id, updatedBook);

        return NoContent();
    }

    [HttpPatch("{id}")]
    public async Task<IActionResult> PatchPrice(string id, [FromBody] JsonPatchDocument<BookDTO> patchDoc)
    {
        if (patchDoc != null)
        {
            var bookDto = new BookDTO();
            patchDoc.ApplyTo(bookDto, ModelState);

            if (!ModelState.IsValid)
            {
                return BadRequest(ModelState);
            }

            var book = await _booksService.GetAsync(id);
            if (book is null)
            {
                return NotFound();
            }
            else
            {
                try
                {
                    book.Price = bookDto.Price;
                    await _booksService.UpdateAsync(id, book);
                    //return NoContent(); // No content to return on successful patch => 204
                    //return Ok(book);
                    return new ObjectResult(book);
                }
                catch (Exception ex)
                {
                    return BadRequest(ex.Message); // Handle specific exceptions as needed
                }
            }
        }
        else
        {
            return BadRequest(ModelState);
        }
    }


    [HttpDelete("{id:length(24)}")]
    public async Task<IActionResult> Delete(string id)
    {
        var book = await _booksService.GetAsync(id);

        if (book is null)
        {
            return NotFound();
        }

        await _booksService.RemoveAsync(id);

        return NoContent();
    }
}