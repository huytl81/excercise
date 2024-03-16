using System;
using System.Text;

namespace Delegate
{
    internal class Delegate
    {
        delegate int myDelegate(string s);

        static int ShowString(string stringValue)
        {
            Console.WriteLine(stringValue);
            return 0;
        }

        static int ConvertStringToInt(string stringValue)
        {
            int valueInt = 0;

            Int32.TryParse(stringValue, out valueInt);
            Console.WriteLine("Đã ép kiểu dữ liệu thành công");

            return valueInt;
        }
        static void NhapVaShowTen(myDelegate showTen)
        {
            Console.WriteLine("Mời nhập tên của bạn:");
            string ten = Console.ReadLine();
            showTen(ten);
        }

        static void Maind(string[] args)
        {
            Console.OutputEncoding = Encoding.Unicode;

            myDelegate showString = new myDelegate(ShowString);
            myDelegate delegateconvertToInt = new myDelegate(ConvertStringToInt);

            //call back function
            NhapVaShowTen(showString);

            string numberSTR = "35";

            int valueConverted = delegateconvertToInt(numberSTR);

            Console.WriteLine("Giá trị đã convert thành int: " + valueConverted);

            Console.ReadLine();

            //==========================================================================
        }
    }
}