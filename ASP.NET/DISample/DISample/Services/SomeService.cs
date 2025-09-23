namespace DISample.Services
{
    public class GuidService : ITransientService, IScopedService, ISingletonService
    {
        private Guid _id;

        public GuidService()
        {
            _id = Guid.NewGuid();
        }

        public Guid GetGuid()
        {
            return _id;
        }
    }
}
