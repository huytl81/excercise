using System.Text;
using System;

namespace EventStandardNet
{
    internal class EventStandardNet
    {
        static void Main(string[] args)
        {
            Console.OutputEncoding = Encoding.Unicode;

            HocSinh hs = new HocSinh();
            hs.NameChanged += Hs_NameChanged;
            hs.Name = "Tên lần 1";
            hs.Name = "Tên lần 2";
            hs.Name = "Tên lần 3";

            Console.ReadLine();
        }

        private static void Hs_NameChanged(object sender, NameChangedEventArgs e)
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


        private event EventHandler<NameChangedEventArgs> _nameChanged;
        public event EventHandler<NameChangedEventArgs> NameChanged
        {
            add
            {
                _nameChanged += value;
            }
            remove
            {
                _nameChanged -= value;
            }
        }

        void OnNameChanged(string name)
        {
            if (_nameChanged != null)
            {
                _nameChanged(this, new NameChangedEventArgs(name));
            }
        }
    }

    public class NameChangedEventArgs : EventArgs
    {
        public string Name { get; set; }
        public NameChangedEventArgs(string name)
        {
            Name = name;
        }
    }

}