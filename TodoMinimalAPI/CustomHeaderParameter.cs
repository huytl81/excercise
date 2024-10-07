using Microsoft.OpenApi.Models;
using Swashbuckle.AspNetCore.SwaggerGen;

namespace TodoMinimalAPI
{
    public class CustomHeaderParameter : IOperationFilter
    {
        public void Apply(OpenApiOperation operation, OperationFilterContext context)
        {
            operation.Parameters =
            [
                new OpenApiParameter
                {
                    Name = "X-Custom-Header",
                    In = ParameterLocation.Header,
                    Description = "Custom header for authentication",
                    Required = true
                },
            ];
        }
    }
}
