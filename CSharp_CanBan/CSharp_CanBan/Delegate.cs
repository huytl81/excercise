using System;
using System.Text;

namespace Delegate
{
    internal class Delegate
    {
        delegate int MyDelegate(string s);

        static int ShowString(string stringValue)
        {
            Console.WriteLine("string is " + stringValue);
            return 0;
        }

        static int ConvertStringToInt(string stringValue)
        {
            int valueInt = 0;

            Int32.TryParse(stringValue, out valueInt);
            Console.WriteLine("Đã ép kiểu dữ liệu thành công");

            return valueInt;
        }
        static void NhapVaShowTen(MyDelegate delShowName)
        {
            Console.WriteLine("Mời nhập tên của bạn:");
            string name = Console.ReadLine();
            delShowName(name);
        }

        static void MainD(string[] args)
        {
            Console.OutputEncoding = Encoding.Unicode;

            var delconvertToInt = new MyDelegate(ConvertStringToInt);
            string numberSTR = "35";
            int valueConverted = delconvertToInt(numberSTR);

            Console.WriteLine("Giá trị đã convert thành int: " + valueConverted);

            Console.ReadLine();

            //==========================================================================

            //MyDelegate delshowString = new MyDelegate(ShowString);
            MyDelegate delshowString = ShowString;
            //call back function
            NhapVaShowTen(delshowString);
        }
    }
}