using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Options;
using Microsoft.IdentityModel.Tokens;
using System.Text;
using TodoMinimalAPI.Data;
using TodoMinimalAPI.Models;

namespace TodoMinimalAPI
{
    public static  class TodoEndpoints
    {
        public static void Map(WebApplication app)
        {
            // Require authorization for role admin and scope greeting_api above
            // create JWT token for testing: dotnet user-jwts create --scope "greetings_api" --role "admin"
            // then test: curl -i -H "Authorization: Bearer {token}" https://localhost:{port}/hello
            // NOTES: remove-item alias:curl if needed
            var jwtSettings = app.Services.GetRequiredService<IOptions<JwtSettings>>().Value;
            var key = jwtSettings.Key;

            app.MapPost("/login", (string username, string password) =>
            {
                if (username == "admin" && password == "123456")
                {
                    var claims = new[]
                    {
                        new System.Security.Claims.Claim("scope", "admin_scope"),
                        new System.Security.Claims.Claim("role", "admin_role"),
                        new System.Security.Claims.Claim("name", username)
                    };

                    var token = new System.IdentityModel.Tokens.Jwt.JwtSecurityToken(
                        claims: claims,
                        expires: DateTime.UtcNow.AddHours(1),
                        signingCredentials: new SigningCredentials(
                            new SymmetricSecurityKey(Encoding.UTF8.GetBytes(key)),
                            SecurityAlgorithms.HmacSha256
                        )
                    );

                    var tokenString = new System.IdentityModel.Tokens.Jwt.JwtSecurityTokenHandler().WriteToken(token);

                    return Results.Ok(new { access_token = tokenString });
                }

                return Results.Unauthorized();
            });

            app.MapGet("/hello", () => "Hello world!").RequireAuthorization("admin_policy");
            app.MapGet("/users/{userId}/books/{bookId}", (int userId, int bookId) => $"The user id is {userId} and the book id is {bookId}");


            var todoItems = app.MapGroup("/todoitems");

            //todoItems.MapGet("/", async (TodoDbContext context) => await context.TodoItems.ToListAsync());
            todoItems.MapGet("/", GetAllTodoItems);
            todoItems.MapGet("/complete", GetCompleteTodoItems);
            todoItems.MapGet("/{id}", GetTodo);
            todoItems.MapPost("/", CreateTodo);
            todoItems.MapPut("/{id}", UpdateTodo);
            todoItems.MapPatch("/{id}", PatchTodo);
            todoItems.MapDelete("/{id}", DeleteTodo);
        }


        static async Task<IResult> GetAllTodoItems(TodoDbContext context)
        {
            return TypedResults.Ok(await context.TodoItems.Select(x => new TodoItemDTO(x)).ToArrayAsync());
            //return TypedResults.Ok(await context.TodoItems.ToListAsync());
        }

        static async Task<IResult> GetCompleteTodoItems(TodoDbContext context)
        {
            return TypedResults.Ok(await context.TodoItems.Where(t => t.IsComplete).Select(x => new TodoItemDTO(x)).ToListAsync());
        }

        static async Task<IResult> GetTodo(int id, TodoDbContext context)
        {
            return await context.TodoItems.FindAsync(id) is TodoItem todoItem
                ? TypedResults.Ok(new TodoItemDTO(todoItem))
                : TypedResults.NotFound();
        }

        static async Task<IResult> CreateTodo(TodoItemDTO todoItemDTO, TodoDbContext context)
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

        static async Task<IResult> PatchTodo(int id, TodoItemDTO todoItemDTO, TodoDbContext context)
        {
            var todoItem = await context.TodoItems.FindAsync(id);

            if (todoItem is null) return TypedResults.NotFound();

            todoItem.Name = todoItemDTO.Name;
            todoItem.IsComplete = todoItemDTO.IsComplete;

            await context.SaveChangesAsync();

            return TypedResults.Ok(todoItem);
            //return TypedResults.NoContent();
        }

        static async Task<IResult> UpdateTodo(int id, TodoItemDTO todoItemDTO, TodoDbContext context)
        {
            var todoItem = await context.TodoItems.FindAsync(id);

            if (todoItem is null) return TypedResults.NotFound();

            todoItem.Name = todoItemDTO.Name;
            todoItem.IsComplete = todoItemDTO.IsComplete;

            await context.SaveChangesAsync();

            return TypedResults.Ok(todoItem);
            //return TypedResults.NoContent();
        }

        static async Task<IResult> DeleteTodo(int id, TodoDbContext context)
        {
            if (await context.TodoItems.FindAsync(id) is TodoItem todoItem)
            {
                context.TodoItems.Remove(todoItem);
                await context.SaveChangesAsync();
                return TypedResults.NoContent();
            }

            return TypedResults.NotFound();
        }
    }
}
