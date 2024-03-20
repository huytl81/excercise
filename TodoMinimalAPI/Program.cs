using Microsoft.EntityFrameworkCore;
using TodoMinimalAPI.Data;
using TodoMinimalAPI.Models;

var builder = WebApplication.CreateBuilder(args);
builder.Services.AddDbContext<TodoContext>(option => option.UseInMemoryDatabase("TodoList"));
builder.Services.AddDatabaseDeveloperPageExceptionFilter();
var app = builder.Build();

var todoItems = app.MapGroup("/todoitems");

todoItems.MapGet("/", GetAllTodoItems);
todoItems.MapGet("/complete", GetCompleteTodoItems);
todoItems.MapGet("/{id}", GetTodo);
todoItems.MapPost("/", CreateTodo);
todoItems.MapPut("/{id}", UpdateTodo);
todoItems.MapDelete("/{id}", DeleteTodo);

app.Run();

static async Task<IResult> GetAllTodoItems(TodoContext context)
{
    return TypedResults.Ok(await context.TodoItems.Select(x=> new TodoItemDTO(x)).ToArrayAsync());
}

static async Task<IResult> GetCompleteTodoItems(TodoContext context)
{
    return TypedResults.Ok(await context.TodoItems.Where(t => t.IsComplete).Select(x => new TodoItemDTO(x)).ToListAsync());
}

static async Task<IResult> GetTodo(int id, TodoContext context)
{
    return await context.TodoItems.FindAsync(id) is TodoItem todoItem
        ? TypedResults.Ok(new TodoItemDTO(todoItem))
        : TypedResults.NotFound();
}

static async Task<IResult> CreateTodo(TodoItemDTO todoItemDTO, TodoContext context)
{
    var todoItem = new TodoItem()
    {
        Name = todoItemDTO.Name,
        IsComplete = todoItemDTO.IsComplete
    };

    context.TodoItems.Add(todoItem);
    await context.SaveChangesAsync();

    return TypedResults.Created($"/todoitems/{todoItem.Id}", todoItem);
}

static async Task<IResult> UpdateTodo(int id, TodoItemDTO todoItemDTO, TodoContext context)
{
    var todoItem = await context.TodoItems.FindAsync(id);

    if (todoItem is null) return TypedResults.NotFound();

    todoItem.Name = todoItemDTO.Name;
    todoItem.IsComplete = todoItemDTO.IsComplete;

    await context.SaveChangesAsync();

    return TypedResults.NoContent();
}

static async Task<IResult> DeleteTodo(int id, TodoContext context)
{
    if (await context.TodoItems.FindAsync(id) is TodoItem todoItem)
    {
        context.TodoItems.Remove(todoItem);
        await context.SaveChangesAsync();
        return TypedResults.NoContent();
    }

    return TypedResults.NotFound();
}