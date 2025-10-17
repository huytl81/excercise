using System;
using System.ComponentModel.DataAnnotations;

namespace Acme.BookStore.Books;

public class CreateUpdateBookDto
{
    [Required]
    public Guid AuthorId { get; set; }

    [Required]
    [StringLength(128)]
    public string Name { get; set; }

    [Required] 
    public BookType Type { get; set; }
    
    [Required]
    [DataType(DataType.DateTime)]
    public DateTime PublishDate { get; set; }
    [Required]
    public float Price { get; set; }
}