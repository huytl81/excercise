﻿namespace Customer.Microservice.Models
{
    public class Customer : BaseModel
    {
        public string Name { get; set; }
        public string Contact { get; set; }
        public string City { get; set; }
        public string Email { get; set; }
    }
}
