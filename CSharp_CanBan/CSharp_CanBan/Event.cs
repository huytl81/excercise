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
            hs.NameChanged += Hs_NameChanged;

            hs.Name = "Kteam";
            Console.WriteLine("Tên từ class: " + hs.Name);

            hs.Name = "HowKteam.com";
            Console.WriteLine("Tên từ class: " + hs.Name);

            Console.ReadLine();

        }

        private static void Hs_NameChanged(string name)
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
                OnNameChanged();
            }
        }

        void OnNameChanged()
        {
            if (NameChanged != null)
            {
                NameChanged(this.Name);
            }
        }
    }

    
}