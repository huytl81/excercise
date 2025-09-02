using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using DISample.Service.DTOs;

namespace DISample.Service
{
    public interface IProductService
    {
        public List<ProductViewModel> GetAll();
    }
}
