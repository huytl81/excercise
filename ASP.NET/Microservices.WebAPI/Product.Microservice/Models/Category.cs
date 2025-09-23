namespace Product.Microservice.Models
{
    public class Category : BaseModel
    {
        public int Id { get; set; }
        public string Name { get; set; }
        public string Description { get; set; }
    }
}
