using System.Text;
using System;

namespace Event
{
    public delegate void DelegateNameChange(string name);

    internal class Event
    {
        static void MainE(string[] args)
        {
            Console.OutputEncoding = Encoding.Unicode;

            HocSinh hs = new HocSinh();
            
            hs.Name = "Kteam";
            Console.WriteLine("Tên từ class: " + hs.Name);

            // start handle event the changing of name
            //hs.EventNameChangedHandler += NameChange;
            hs.EventNameChangedHandler += new DelegateNameChange(NameChange);
            Console.Write("Sửa lại tên học sinh:");
            hs.Name = Console.ReadLine();
        }

        private static void NameChange(string name)
        {
            Console.WriteLine("Tên mới: " + name);
        }
    }

    public class HocSinh
    {
        public event DelegateNameChange EventNameChangedHandler;

        private string _name;
        public string Name
        {
            //get => _name;
            get { return _name; }

            set
            {
                _name = value;
                OnNameChange();
            }
        }

        void OnNameChange()
        {
            if (EventNameChangedHandler != null)
            {
                EventNameChangedHandler(this.Name);
            }
        }
    }

    
}