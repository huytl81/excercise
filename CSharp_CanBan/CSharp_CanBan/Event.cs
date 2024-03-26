using System.Text;
using System;
using EventStandardNet;

namespace Event
{
    public delegate void UpdateNameChangeHandler(string name);

    internal class Event
    {
        static void MainE(string[] args)
        {
            Console.OutputEncoding = Encoding.Unicode;

            HocSinh hs = new HocSinh();
            hs.NameChanged += HSNameChanged;

            hs.Name = "Kteam";
            Console.WriteLine("Tên từ class: " + hs.Name);

            hs.Name = "HowKteam.com";
            Console.WriteLine("Tên từ class: " + hs.Name);

            Console.ReadLine();

        }

        static void HSNameChanged(string name)
        {
            Console.WriteLine("Tên mới: " + name);
        }
    }

    public class HocSinh
    {
        public event UpdateNameChangeHandler NameChanged;

        private string _name;
        public string Name
        {
            //get => _name;
            get { return _name; }

            set
            {
                _name = value;
                OnNameChanged(value);
                //if (NameChanged != null)
                //{
                //    NameChanged(Name);
                //}
            }
        }

        void OnNameChanged(string name)
        {
            if (NameChanged != null)
            {
                NameChanged(this.Name);
            }
        }
    }

    
}