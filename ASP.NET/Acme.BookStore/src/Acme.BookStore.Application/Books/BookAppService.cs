using System;
using System.Collections.Generic;
using System.Linq;
using System.Linq.Dynamic.Core;
using System.Threading.Tasks;
using Acme.BookStore.Authors;
using Acme.BookStore.Permissions;
using Microsoft.AspNetCore.Authorization;
using Volo.Abp.Application.Dtos;
using Volo.Abp.Application.Services;
using Volo.Abp.Domain.Entities;
using Volo.Abp.Domain.Repositories;

namespace Acme.BookStore.Books;

[Authorize(BookStorePermissions.Books.Default)]
public class BookAppService : CrudAppService<Book, BookDto, Guid, PagedAndSortedResultRequestDto, CreateUpdateBookDto>, IBookAppService
{
    private readonly IAuthorRepository _authorRepository;

    public BookAppService(IRepository<Book, Guid> repository, IAuthorRepository authorRepository) : base(repository)
    {
        _authorRepository = authorRepository;
        GetPolicyName = BookStorePermissions.Books.Default;
        GetListPolicyName = BookStorePermissions.Books.Default;
        CreatePolicyName = BookStorePermissions.Books.Create;
        UpdatePolicyName = BookStorePermissions.Books.Edit;
        DeletePolicyName = BookStorePermissions.Books.Delete;
    }

    public override async Task<BookDto> GetAsync(Guid id)
    {
        IQueryable<Book> bq = await Repository.GetQueryableAsync();
        IQueryable<Author> aq = await _authorRepository.GetQueryableAsync();

        var query = from book in bq
            join author in aq 
                on book.AuthorId equals author.Id
            where book.Id == id
            select new { book, author };
        
        var result = await AsyncExecuter.FirstOrDefaultAsync(query);
        if (result == null)
        {
            throw new EntityNotFoundException(typeof(Book), id);
        }

        var bookDto = ObjectMapper.Map<Book, BookDto>(result.book);
        bookDto.AuthorName = result.author.Name;
        return bookDto;
    }
        
    public override async Task<PagedResultDto<BookDto>> GetListAsync(PagedAndSortedResultRequestDto input)
    {
        //Get the IQueryable<Book> from the repository
        IQueryable<Book> bq = await Repository.GetQueryableAsync();
        IQueryable<Author> aq = await _authorRepository.GetQueryableAsync();

        //Prepare a query to join books and authors
        var query = from book in bq
            join author in aq 
                on book.AuthorId equals author.Id
            select new {book, author};

        //Paging
        if (input.Sorting != null)
        {
            query = query.OrderBy(NormalizeSorting(input.Sorting)).Skip(input.SkipCount).Take(input.MaxResultCount);
        }

        //Execute the query and get a list
        var result = await AsyncExecuter.ToListAsync(query);

        //Convert the query result to a list of BookDto objects
        IEnumerable<BookDto> iebookDtos = result.Select(x =>
        {
            BookDto bookDto = ObjectMapper.Map<Book, BookDto>(x.book);
            bookDto.AuthorName = x.author.Name;
            return bookDto;
        });
        
        List<BookDto> bookDtos = iebookDtos.ToList();

        //Get the total count with another query
        var totalCount = await Repository.GetCountAsync();

        return new PagedResultDto<BookDto>(
            totalCount,
            bookDtos
        );
    }

    public async Task<ListResultDto<AuthorLookupDto>> GetAuthorLookupAsync()
    {
        var authors = await _authorRepository.GetListAsync();

        return new ListResultDto<AuthorLookupDto>(
            ObjectMapper.Map<List<Author>, List<AuthorLookupDto>>(authors)
        );
    }

    private static string NormalizeSorting(string sorting)
    {
        if (sorting.IsNullOrEmpty())
        {
            return $"book.{nameof(Book.Name)}";
        }

        if (sorting.Contains("authorName", StringComparison.OrdinalIgnoreCase))
        {
            return sorting.Replace(
                "authorName",
                "author.Name",
                StringComparison.OrdinalIgnoreCase
            );
        }

        return $"book.{sorting}";
    }
}
