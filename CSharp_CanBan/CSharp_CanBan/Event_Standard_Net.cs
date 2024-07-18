using System.Text;
using System;

namespace EventStandardNet
{
    internal class EventStandardNet
    {
        static void ESMain(string[] args)
        {
            Console.OutputEncoding = Encoding.Unicode;

            HocSinh hs = new HocSinh();
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
                OnNameChanged(value);
            }
        }

        //public int Age
        //{
        //    get => _age;
        //    set => _age = value;
        //}
        //public int Age { get; set; }
        


        private event EventHandler<NameChangeEventArgs> _eventNameChangeHandler;
        internal event EventHandler<NameChangeEventArgs> EventNameChangeHandler
        {
            add
            {
                _eventNameChangeHandler += value;
            }
            remove
            {
                _eventNameChangeHandler -= value;
            }
        }

        void OnNameChanged(string name)
        {
            if (_eventNameChangeHandler != null)
            {
                _eventNameChangeHandler(this, new NameChangeEventArgs(name));
            }
        }
    }
    
    internal class NameChangeEventArgs : EventArgs
    {
        public string Name { get; set; }
        public NameChangeEventArgs(string name)
        {
            Name = name;
        }
    }

}