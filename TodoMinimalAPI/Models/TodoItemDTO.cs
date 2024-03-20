namespace TodoMinimalAPI.Models
{
    public class TodoItemDTO
    {
        public int Id { get; set; }
        public string? Name { get; set; }
        public bool IsComplete { get; set; }

        public TodoItemDTO() { }
        //public TodoItemDTO(TodoItem todoItem)
        //{
        //    Id = todoItem.Id;
        //    Name = todoItem.Name;
        //    IsComplete = todoItem.IsComplete;
        //}
        public TodoItemDTO(TodoItem todoItem) => (Id, Name, IsComplete) = (todoItem.Id, todoItem.Name, todoItem.IsComplete) ;
    }
}
