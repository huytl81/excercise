using System;
using System.Text;

namespace Delegate
{
    internal class DelegateExample
    {
        //Func<T, TResult>: delegate trả về giá trị.
        //Action<T>: delegate void.
        //Predicate<T>: delegate bool.
        delegate int mydelegate(string s);

        static int ShowString(string stringValue)
        {
            Console.WriteLine("Your name is " + stringValue);
            return 0;
        }

        static int ConvertStringToInt(string stringValue)
        {
            bool b = Int32.TryParse(stringValue, out int valueInt);
            if (b)
            {
                Console.WriteLine("Đã ép kiểu dữ liệu thành công: {0}", valueInt);
                return valueInt;
            }
            Console.WriteLine("Không thể chuyển thành số");
            return 0;
        }

        //sử dụng built-in delegate Func
        static void NhapVaShowTen(Func<string, int> delShowName)
        {
            Console.WriteLine("Mời nhập tên của bạn:");
            string name = Console.ReadLine();
            delShowName(name);
        }

        // sử dụng custom delegate
        //static void NhapVaShowTen(mydelegate delShowName)
        //{
        //    Console.WriteLine("Mời nhập tên của bạn:");
        //    string name = Console.ReadLine();
        //    delShowName(name);
        //}

        //static void Main(string[] args)
        //{
        //    Console.OutputEncoding = Encoding.Unicode;

        //    mydelegate customdel = ConvertStringToInt;
        //    string numberSTR = "35";
        //    int valueConverted = customdel(numberSTR);

        //    Console.WriteLine("Giá trị đã convert thành int: " + valueConverted);

        //    Console.ReadLine();

        //    //sử dụng built-in delegate
        //    // void thi dung Action<string> show = ShowString;
        //    Func<string,int> delshowname = ShowString;
        //    NhapVaShowTen(delshowname);

        //    //sử dụng custom delegate
        //    //var delshowname = new mydelegate(ShowString);
        //    //NhapVaShowTen(delshowname);

        //    //multicast delegate
        //    mydelegate a = ConvertStringToInt;
        //    mydelegate b = ShowString;
        //    var both = b + a;
        //    int kq = both("12345");
        //    Console.WriteLine("Kết quả trả về: " + kq);
        //}
    }
}