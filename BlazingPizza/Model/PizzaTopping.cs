namespace BlazingPizza
{
    public class PizzaTopping
    {
        public int ToppingId { get; set; }
        public int PizzaId { get; set; }
        public Topping Topping { get; set; }
    }
}
