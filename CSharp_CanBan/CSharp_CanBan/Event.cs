using System.Text;
using System;

namespace Event
{
    public delegate void myDelegateNameHandler(string name);

    internal class Event
    {
        static void Maine(string[] args)
        {
            Console.OutputEncoding = Encoding.Unicode;

            HocSinh hs = new HocSinh();
            hs.my_Event_NameChanged += Hs_my_Event_NameChanged; ;

            hs.Name = "Kteam";
            Console.WriteLine("Tên từ class: " + hs.Name);
            hs.Name = "HowKteam.com";
            Console.WriteLine("Tên từ class: " + hs.Name);

            Console.ReadLine();

        }

        static void Hs_my_Event_NameChanged(string name)
        {
            Console.WriteLine("Tên mới: " + name);
        }
    }

    public class HocSinh
    {
        public event myDelegateNameHandler my_Event_NameChanged;

        private string _name;
        public string Name
        {
            get => _name;

            set
            {
                _name = value;
                if (my_Event_NameChanged != null)
                {
                    my_Event_NameChanged(Name);
                }
            }
        }
    }

    
}