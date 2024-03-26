namespace DISample.Services
{
    public class SomeService : ITransientService, IScopedService, ISingletonService
    {
        private Guid _id;

        public SomeService()
        {
            _id = Guid.NewGuid();
        }

        public Guid GetGuid()
        {
            return _id;
        }
    }
}
