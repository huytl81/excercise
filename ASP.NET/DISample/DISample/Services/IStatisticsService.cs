using DISample.Service.DTOs;

namespace DISample.Services
{
    public interface IStatisticsService
    {
        int GetCount();
        int GetCompletedCount();
        double GetAveragePriority();
        List<TodoItem> GetAllItems();
    }
}
