using System.Text;
using System;

namespace EventStandardNet
{
    internal class EventStdExample
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = Encoding.Unicode;

            HocSinh hs = new HocSinh(){
                Name = "Nguyễn Văn A"
            };

            hs.EventNameChangeHandler += NameChange;
            
            hs.Name = "Tên lần 1";
            hs.Name = "Tên lần 2";
            hs.Name = "Tên lần 3";

            Console.ReadLine();
        }

        private static void NameChange(object sender, NameChangeEventArgs e)
        {
            Console.WriteLine("Tên có thay đổi: " + e.Name);
        }
    }

    public class HocSinh
    {
        private string _name;

        public string Name
        {
            get => _name;
            set
            {
                _name = value;
                OnChange(value);
            }
        }

        //public int Age
        //{
        //    get => _age;
        //    set => _age = value;
        //}
        //public int Age { get; set; }
        

        private event EventHandler<CustomEventArgs> _customeEventHandler;
        internal event EventHandler<CustomEventArgs> CustomeEventHandler
        {
            add
            {
                _customeEventHandler += value;
            }
            remove
            {
                _customeEventHandler -= value;
            }
        }

        void OnChange(string name)
        {
            if (_customeEventHandler != null)
            {
                _customeEventHandler(this, new CustomEventArgs(name));
            }
        }
    }
    
    internal class CustomEventArgs : EventArgs
    {
        public string Name { get; set; }
        public CustomEventArgs(string name)
        {
            Name = name;
        }
    }

}