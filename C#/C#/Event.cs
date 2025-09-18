using System.Text;
using System;

namespace EventExample
{
    public delegate void customDelegate(string name);
    
    internal class EventExample
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = Encoding.Unicode;

            HocSinh hs = new HocSinh()
            {
                Name = "Nguyễn Văn A"
            };
            //HocSinh hs = new HocSinh();
            //hs.Name = "Kteam";

            Console.WriteLine("Tên từ class: " + hs.Name);

            // register event handler
            //hs.customEventHandler += new customDelegate(NameChange);
            hs.customEventHandler += NameChange;
            
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
        public event customDelegate customEventHandler;

        private string _name;
        public string Name
        {
            //get => _name;
            get { 
                return _name; 
            }

            set {
                _name = value;
                OnChange();
            }
        }

        void OnChange()
        {
            if (customEventHandler != null)
            {
                customEventHandler(this.Name);
            }
        }
    }
}