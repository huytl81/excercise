//using Microsoft.EntityFrameworkCore;
//using TodoMinimalAPI.Data;
//using TodoMinimalAPI.Models;

//var builder = WebApplication.CreateBuilder(args);
//builder.Services.AddDbContext<TodoContext>(option => option.UseInMemoryDatabase("TodoList"));
//builder.Services.AddDatabaseDeveloperPageExceptionFilter();
//var app = builder.Build();

//var todoItems = app.MapGroup("/todoitems");

//todoItems.MapGet("/", async (TodoContext context) => 
//    await context.TodoItems.ToListAsync());

//todoItems.MapGet("/complete", async (TodoContext context) => 
//    await context.TodoItems.Where(t => t.IsComplete == true).ToListAsync());

//todoItems.MapGet("/{id}", async (int id, TodoContext context) => 
//    await context.TodoItems.FindAsync(id)
//        is TodoItem todo ? Results.Ok(todo) : Results.NotFound());

//todoItems.MapPost("/", async (TodoItem todo, TodoContext context) => 
//{
//    context.TodoItems.Add(todo);
//    await context.SaveChangesAsync();

//    return Results.Created($"/todoitems/{todo.Id}", todo);
//});

//todoItems.MapPut("/{id}", async (int id, TodoItem inputTodo, TodoContext context) =>
//{
//    var todo = await context.TodoItems.FindAsync(id);

//    if (todo is null) return Results.NotFound();

//    todo.Name = inputTodo.Name;
//    todo.IsComplete = inputTodo.IsComplete;

//    await context.SaveChangesAsync();

//    return Results.NoContent();
//});

//todoItems.MapDelete("/{id}", async (int id, TodoContext context) =>
//{
//    if (await context.TodoItems.FindAsync(id) is TodoItem todo)
//    {
//        context.TodoItems.Remove(todo);
//        await context.SaveChangesAsync();
//        return Results.NoContent();
//    }

//    return Results.NotFound();
//});

//app.Run();
