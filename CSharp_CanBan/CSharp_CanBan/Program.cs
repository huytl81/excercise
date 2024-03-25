using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Text.RegularExpressions;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace Program
{
    internal class Program
    {
        /// <summary>
        ///  hai biến firstNumber và secondNumber hiện là biến toàn cục của các hàm nằm bên trong class Program nhưng lại là biến cục bộ của class Program
        ///  Cần có từ khóa static vì các hàm sử dụng nó đều có từ khóa static
        /// </summary>

        static int _firstNumber = 5;
        static int _secondNumber = 10;

        static void Main(string[] args)
        {
            int myvalue = 10;
            object obj = myvalue;
            int newvalue = 0;
            if (obj is int)
            {
                newvalue = (int)obj;
            }

            dynamic str = "13";
            int? mystr = str as int?;

            
            Console.WriteLine("My object is: {0}", obj);
            Console.WriteLine("My newvalue is: {0}", newvalue);
            Console.WriteLine("My dynamic is: {0}", str++);

            int refvalue = 5;
            int outvalue;
            Console.WriteLine("Value ref-out before increase: {0}", refvalue);
            //IncreaseValueRef(ref refvalue);
            IncreaseValueOut(out outvalue);
            Console.WriteLine("Value ref-out after increase: {0}", outvalue);
            Console.ReadKey();

            // Array 
            int[] intArryaInts = new Int32[] { 1, 2, 3 };
            Console.WriteLine(intArryaInts[1]);

            string[] strArray = new string[5];
            strArray = new[] { "A", "B", "C","D" };
            Console.WriteLine(strArray[3]);

            string[] arrnames = new[] { "Huy", "Binh", "Ha", "Xuyen" };
            Console.WriteLine(arrnames[3]);

            // Array 2 directions
            string[,] arrStrings = new string[2, 3] { { "Huy", "42", "10" }, { "Ha", "42", "9" } };
            Console.WriteLine(arrStrings[1,0]);

            // Khai báo, cấp phát và khởi tạo mảng 3 chiều kiểu int và tên là Mang3Chieu
            int[,,] Mang3Chieu = new int[,,]
            {
                {
                    {1, 2, 3},
                    {4, 5, 6}
                },
                {
                    {7, 8, 9},
                    {10, 11, 12}
                },
                {
                    {12, 18, 19},
                    {110, 111, 112}
                }
                ,
                {
                    {212, 218, 219},
                    {210, 111, 112}
                }
            };
            /*
            * Truy xuất đến phần tử có các chỉ số lần lượt là 1 1 2
            */
            Console.WriteLine(Mang3Chieu[2, 1, 2]);

            //jagged array
            int[][] jInts = new int[][] {
                new int[] {1, 2, 3},
                new int[] {6, 7, 8}
            };
            Console.WriteLine(jInts[0][2]);

            // Mảng Can chứa các giá trị can tương ứng theo bảng can
            string[] arrCan = { "Canh", "Tan", "Nham", "Quy", "Giap", "At", "Binh", "Dinh", "Mau", "Ky" };

            // Mảng Chi chứa các giá trị chi tương ứng theo bảng chi
            string[] arrChi = { "Than", "Dau", "Tuat", "Hoi", "Ty", "Suu", "Dan", "Mao", "Thin", "Ty", "Ngo", "Mui" };

            int Year; // Biến chứa giá trị năm cần tính.
            bool isYear;
            string Can = "", Chi = ""; // Biến chứa kết quả.

            Console.Write(" Moi ban nhap mot nam bat ky: ");
            isYear = Int32.TryParse(Console.ReadLine(), out Year); // Nhập năm dương lịch và ép kiểu về kiểu số nguyên

            if (isYear)
            {
                switch (Year % 10) // Tìm Can như thuật toán đã trình bày.
                {
                    case 0: // Mỗi case này tương ứng một kết quả cần tra cứu trong bảng tra cứu Can
                        Can = "Canh"; // Giá trị tương ứng với mỗi case
                        break;
                    case 1:
                        Can = "Tan";
                        break;
                    case 2:
                        Can = "Nham";
                        break;
                    case 3:
                        Can = "Quy";
                        break;
                    case 4:
                        Can = "Giap";
                        break;
                    case 5:
                        Can = "At";
                        break;
                    case 6:
                        Can = "Binh";
                        break;
                    case 7:
                        Can = "Dinh";
                        break;
                    case 8:
                        Can = "Mau";
                        break;
                    case 9:
                        Can = "Ky";
                        break;
                }

                switch (Year % 12) // Tìm Chi như thuật toán đã trình bày
                {
                    case 0: // Mỗi case này tương ứng một kết quả cần tra cứu trong bảng tra cứu Chi
                        Chi = "Than"; // Giá trị tương ứng với mỗi case
                        break;
                    case 1:
                        Chi = "Dau";
                        break;
                    case 2:
                        Chi = "Tuat";
                        break;
                    case 3:
                        Chi = "Hoi";
                        break;
                    case 4:
                        Chi = "Ty";
                        break;
                    case 5:
                        Chi = "Suu";
                        break;
                    case 6:
                        Chi = "Dan";
                        break;
                    case 7:
                        Chi = "Mao";
                        break;
                    case 8:
                        Chi = "Thin";
                        break;
                    case 9:
                        Chi = "Ti";
                        break;
                    case 10:
                        Chi = "Ngo";
                        break;
                    case 11:
                        Chi = "Mui";
                        break;
                }
            }

            Console.WriteLine("Nam {0} co nam am lich la: {1} {2}", Year, Can, Chi); // Nối Can và Chi lại để được năm âm lịch
            Console.WriteLine($"Nam {Year} co nam am lich la: {arrCan[Year%10]} {arrChi[Year % 12]}"); // Nối Can và Chi lại để được năm âm lịch

            Student sv = new Student();
            Console.WriteLine("Nhap thong tin sinh vien:");
            NhapThongTinSinhVien(out sv);
            Console.WriteLine("Thong tin sinh vien vua nhap:");
            XuatThongTinSinhVien(sv);
            Console.WriteLine("Diem trung binh cua sinh vien vua nhap: {0}", DiemTrungBinh(sv));

            // Regular Expression example
            Regex reg = new Regex(@"(?<times>(\d|:)+)\s" + @"(?<company>\S+)\s" + @"(?<ip>(\d|\.)+)\s" + @"(?<company>\S+)\s" + @"(?<company>\S+)");
            foreach (Match item in reg.Matches("10:30:15 IBM 192.168.1.2 INTEL APPLE"))
            {
                Console.WriteLine(" time: " + item.Groups["times"]);
                Console.WriteLine(" ip: " + item.Groups["ip"]);
                Console.Write(" company: ");
                /*
                    Lấy ra tất cả các capture bắt được trong group company và duyệt lần lượt chúng
                 * Sau đó ta có thể sử dụng hàm ToString() hoặc thuộc tính Value để lấy giá trị của Capture
                 */
                foreach (Capture i in item.Groups["company"].Captures)
                {
                    Console.Write(i.ToString() + " ");
                }

            }

            Console.ReadKey();
            // ==================================== END BASIC ========================================================//

            int d, m, y = 0;
            var myCurrent = GetCurrentDayMonthYear();
            GetCurrentDay(out d,out m,out y);

            Console.WriteLine("Day: {0}, Month: {1}, Year: {2}", d, m, y);
            Console.WriteLine("Day: {0}, Month: {1}, Year: {2}", myCurrent.Item1, myCurrent.Item2, myCurrent.Item3);

            // Khởi tạo Tuple thông qua phương thức Create
            var myTuple = Tuple.Create<int, string>(1, "HowKteam");
            var myTuple2 = new Tuple<int,string>(2, "Hello world");

            Console.WriteLine("ID: {0}, Name: {1}", myTuple.Item1, myTuple.Item2);

            // Tạo 1 Queue rỗng
            Queue MyQueue4 = new Queue();

            // Thực hiện thêm vài phần tử vào Queue thông qua hàm Enqueue.
            MyQueue4.Enqueue("HowKteam");
            MyQueue4.Enqueue("Free");
            MyQueue4.Enqueue("Education");

            // Thử sử dụng các phương thức của Queue.
            Console.WriteLine(" So phan tu hien tai cua Queue la: {0}", MyQueue4.Count);

            // Lưu ý ở đây ta chỉ muốn xem giá trị mà không muốn nó khỏi Queue thì ta sẽ dùng Peek.
            Console.WriteLine(" Phan tu dau cua Queue la: {0}", MyQueue4.Peek());

            // Thử kiểm tra lại số phần tử để chắc chắn rằng hàm Peek không xoá phần tử ra khỏi Queue.
            Console.WriteLine(" So phan tu cua Queue sau khi goi ham Peek: {0}", MyQueue4.Count);

            // Thực hiện xoá các phần tử ra khỏi Queue thông qua hàm Dequeue.
            Console.WriteLine(" Popping...");
            int Length = MyQueue4.Count;
            for (int i = 0; i < Length; i++)
            {
                Console.Write(" " + MyQueue4.Dequeue());
            }
            Console.WriteLine();

            // Kiểm tra lại số phần tử của Queue sau khi Pop
            Console.WriteLine(" So phan tu cua Queue sau khi Pop la: {0}", MyQueue4.Count);


            SortedList MySL6 = new SortedList(new SortPersons());
            MySL6.Add(new Person("HowKteam", 20), 30);
            MySL6.Add(new Person("Kteam", 2), 15);
            Console.WriteLine("Danh sach Person dc sap xep: ");
            foreach (DictionaryEntry item in MySL6)
            {
                Console.WriteLine(item.Key + "\t" + item.Value);
            }

            // Tạo một Hashtable đơn giản với 3 phần tử
            Hashtable hash = new Hashtable();
            hash.Add("K", "Kteam");
            hash.Add("H", "HowKteam");
            hash.Add("FE", "Free Education");

            /*
             * Duyệt qua các phần tử trong Hashtable.
             * Vì mỗi phần tử là 1 DictionaryEntry nên ta chỉ định kiểu dữ liệu cho item là DictionaryEntry luôn.
             * Thử in ra màn hình cặp Key - Value của mỗi phần tử được duyệt.
             */
            foreach (DictionaryEntry item in hash)
            {
                Console.WriteLine(item.Key + "\t" + item.Value);
            }


            // Tạo 1 danh sách kiểu ArrayList rỗng
            ArrayList arrPersons = new ArrayList();

            // Thêm 3 Person vào danh sách
            arrPersons.Add(new Person("Nguyen Van A", 18));
            arrPersons.Add(new Person("Nguyen Van B", 25));
            arrPersons.Add(new Person("Nguyen Van C", 20));

            // In thử danh sách Person ban đầu ra.
            Console.WriteLine("Danh sach Person ban dau: ");
            foreach (Person item in arrPersons)
            {
                Console.WriteLine(item.ToString());
            }

            /*
             * Thực hiện sắp xếp danh sách Person theo tiêu chí đã được định nghĩa
             * trong phương thức Compare của lớp SortPerson (tuổi tăng dần).
             */
            arrPersons.Sort(new SortPersons());

            // In danh sách Person đã được sắp xếp ra màn hình.
            Console.WriteLine();
            Console.WriteLine("Danh sach Person da duoc sap xep theo tuoi tang dan: ");
            foreach (Person item in arrPersons)
            {
                Console.WriteLine(item.ToString());
            }

            Animal cat = new Cat();
            Animal dog = new Dog();

            cat.Speak();
            dog.Speak();

            /* In ra màn hình giá trị của thuộc tính màu chủ đạo */
            Console.WriteLine(" Mau chu dao cua hom nay: " + Color.MauChuDao);

            /*
                Khởi tạo 2 đối tượng thuộc lớp Animal là:
                + Dog có chiều cao 50cm và cân nặng 2kg.
                + Cat có chiều cao 30cm và cân nặng 1kg.
            */
            Animal Dog = new Dog();
            Dog.Weight = 2; // gán giá trị cho các thuộc tính của đối tượng
            Dog.Height = 50;


            Animal Cat = new Cat();
            Cat.Weight = 1;
            Cat.Height = 30;


            Dog.Info(typeof(Dog)); // gọi phương thức của đối tượng

            Cat.Info(typeof(Cat));

            Console.WriteLine(SumTwoNumber());
            Console.ReadKey();

            // Kiểu số thực
            float bienFloat = 9.9f; // Giá trị của biến kiểu float phải có hậu tố f hoặc F. 
            double bienDouble = 10.9; // Giá trị của biến kiểu double không cần hậu tố.
            decimal bienDecimal = 11.9m; // Giá trị của biến kiểu decimal phải có hậu tố m.

            string name, age, address;

            Console.WriteLine(bienFloat);
            Console.WriteLine(bienDouble);
            Console.WriteLine(bienDecimal);

            int N = 10;
            int M = 20;

            char drawChar = '*';
            char insideChar = ' ';


            // Vẽ từ trên xuống
            for (int i = 0; i < N; i++)
            {
                // Vẽ từ trái sang
                for (int j = 0; j < M; j++)
                {
                    /*
                     * Nếu đang ở tọa độ là cạnh trên hoặc dưới i % (N - 1) == 0
                     * hoặc đang ở cạnh trái hoặc phải (j % (M - 1) == 0)
                     * mà không nằm ở cạnh trên hoặc dưới (i % (N - 1) != 0)
                     * ((i % (N - 1) != 0) && (j % (M - 1) == 0))
                     * thì vẽ ra ký tự của hình chữ nhật
                     * ngược lại vẽ ra ký tự không thuộc hình chữ nhật
                     */

                    if (i % (N - 1) == 0 || ((i % (N - 1) != 0) && (j % (M - 1) == 0)))
                    {
                        Console.Write(drawChar);    // lúc này là ký tự *
                    }
                    else
                    {
                        Console.Write(insideChar);  // lúc này là ký tự rỗng ' '
                    }
                }
                //mỗi lần vẽ xong một hàng thì xuống dòng
                Console.WriteLine();
            }
            Console.ReadKey();

            Console.ReadLine();

            Console.Write("Enter your name:");
            name = Console.ReadLine();
            Console.WriteLine("HowKteam.com hello: {0}", name);
            Console.Write("Enter your age:");
            age = Console.ReadLine();
            Console.Write("Enter your address:");
            address = Console.ReadLine();
            Console.WriteLine("Your name is {0}, {1} years old, live in {2}", name, age, address);

            Console.WriteLine(sizeof(float));
            Console.WriteLine(typeof(string));

            string strInt;
            int intNum;
            string result;
            Console.Write("Enter integer number:");
            strInt = Console.ReadLine();
            intNum = Int32.Parse(strInt);
            result = (intNum % 2 == 0) ? "even" : "odd";
            Console.WriteLine("{0} is {1}", strInt, result);


            Console.ReadKey();
        }

        static void IncreaseValueRef(ref int refvalue)
        {
            refvalue++;
        }

        static void IncreaseValueOut(out int outvalue)
        {
            outvalue = 0;
            outvalue++;
        }

        /// <summary>
        /// hàm trả ra kết quả tổng của 2 số firstNumber và secondNumber
        /// </summary>
        /// <returns></returns>
        static int SumTwoNumber()
        {
            return _firstNumber + _secondNumber;
        }

        static void GetCurrentDay(out int currday, out int currmonth, out int curryear)
        {
            currday = 0;
            currmonth = 0;
            curryear = 0;

            DateTime now = DateTime.Now; // lấy ngày giờ hiện tại của hệ thống.
            /* Sử dụng Constructor của Tuple<> để trả về hoặc có thể sử dụng phương thức Create đã trình bày ở trên. */
            currday = now.Day;
            currmonth = now.Month;
            curryear = now.Year;
        }

        /// <summary>
        /// Phương thức trả về 1 Tuple có 3 thuộc tính (cả 3 đều có kiểu dữ liệu là int)
        /// </summary>
        /// <returns>
        /// Huy Ta - Tra ve 1 new tuple
        /// </returns>

        static Tuple<int, int, int> GetCurrentDayMonthYear()
        {
            // lấy ngày giờ hiện tại của hệ thống.
            DateTime now = DateTime.Now;
            /* Sử dụng Constructor của Tuple<> để trả về hoặc có thể sử dụng phương thức Create đã trình bày ở trên. */
            return new Tuple<int, int, int>(now.Day, now.Month, now.Year);
        }

        static void NhapThongTinSinhVien(out Student sv)
        {
            Console.WriteLine("=================");
            Console.Write("Nhap ma so sinh vien:");
            sv.MaSo = int.Parse(Console.ReadLine() ?? string.Empty);
            Console.Write("Nhap ho ten sinh vien:");
            sv.HoTen = Console.ReadLine();
            Console.Write("Nhap diem toan:");
            sv.DiemToan = double.Parse(Console.ReadLine() ?? string.Empty);
            Console.Write("Nhap diem ly:");
            sv.DiemLy = double.Parse(Console.ReadLine() ?? string.Empty);
            Console.Write("Nhap diem van:");
            sv.DiemVan = double.Parse(Console.ReadLine() ?? string.Empty);
        }
        static void XuatThongTinSinhVien(Student sv)
        {
            Console.WriteLine("=================");
            Console.WriteLine($"Ma so sinh vien: {sv.MaSo}");
            Console.WriteLine($"Ho ten sinh vien: {sv.HoTen}");
            Console.WriteLine($"Diem toan: {sv.DiemToan}");
            Console.WriteLine($"Diem ly: {sv.DiemLy}");
            Console.WriteLine($"Diem van: {sv.DiemVan}");
        }

        static double DiemTrungBinh(Student sv)
        {
            var dtb = (sv.DiemToan + sv.DiemLy + sv.DiemVan) / 3;
            return dtb;
        }
    }

    abstract class Animal
    {

        public double Weight;
        public double Height;

        //public virtual void Speak()
        //{
        //    Console.WriteLine(" Animal is speaking. . .");
        //}

        public abstract void Speak();

        public void Info(object animal)
        {

            /*
                Các phương thức bên trong lớp có thể gọi đến các thành phần khác (bao gồm thuộc tính và phương thức) trong lớp đó.
                Giá trị của các thuộc tính này có thể được khởi tạo đâu đó trong lớp hoặc từ bên ngoài truyền vào.
            */
            if (((Type)animal).Name == "Dog")
            {
                Console.WriteLine("Dog Height: " + Height + " Weight: " + Weight);
            }
            else
            {
                Console.WriteLine("Cat Height: " + Height + " Weight: " + Weight);
            }
        }
    }

    class Cat : Animal
    {
        public override void Speak()
        {
            Console.WriteLine(" Cat is speaking. . .");
        }
    }


    class Dog : Animal
    {
        public override void Speak()
        {
            Console.WriteLine(" Dog is speaking. . .");
        }
    }

    static class Color
    {
        /* Giả sử màu chủ đạo là 1 chuỗi ký tự lưu tên màu tương ứng */
        public static string MauChuDao;
        /* Dùng static constructor để kiểm tra ngày hiện tại và khởi tạo giá trị cho biến tĩnh MauChuDao */
        static Color()
        {
            /* Khai báo đối tượng ngày giờ và lấy ngày giờ hiện tại của hệ thống */
            DateTime now = DateTime.Now;

            /* lấy ra thứ của ngày hiện tại và so sánh với 7 ngày trong tuần */
            switch (now.DayOfWeek)
            {
                case DayOfWeek.Friday:
                    MauChuDao = "Black";
                    break;
                case DayOfWeek.Monday:
                    MauChuDao = "Blue";
                    break;
                case DayOfWeek.Saturday:
                    MauChuDao = "Green";
                    break;
                case DayOfWeek.Sunday:
                    MauChuDao = "Yellow";
                    break;
                case DayOfWeek.Thursday:
                    MauChuDao = "Pink";
                    break;
                case DayOfWeek.Tuesday:
                    MauChuDao = "Red";
                    break;
                case DayOfWeek.Wednesday:
                    MauChuDao = "Purple";
                    break;
            }
        }
    }

    public class Person
    {
        private string name;
        private int age;

        public string Name
        {
            get { return name; }
            set { name = value; }
        }

        public int Age
        {
            get { return age; }
            set { age = value; }
        }

        /// <summary>
        /// Tạo 1 constructor có tham số để tiện cho việc khởi tạo nhanh đối tượng Person với các giá trị cho sẵn.
        /// </summary>
        /// <param name="Name"></param>
        /// <param name="Age"></param>
        public Person(string Name, int Age)
        {
            this.Name = Name;
            this.Age = Age;
        }

        /// <summary>
        /// Override phương thức ToString để khi cần có thể in thông tin của object ra cho nhanh.
        /// </summary>
        /// <returns></returns>
        public override string ToString()
        {
            return "Name: " + name + " | Age: " + age;
        }
    }

    struct Student
    {
        public int MaSo;
        public string HoTen;
        public double DiemToan;
        public double DiemLy;
        public double DiemVan;
    }

    public class SortPersons : IComparer
    {
        public int Compare(object x, object y)
        {
            // Ép kiểu 2 object truyền vào về Person.
            Person p1 = x as Person;
            Person p2 = y as Person;

            /*
             * Vì có thể 2 object truyền vào không phải Person khi đó ta không thể so sánh được.
             * Trường hợp này tốt nhất ta nên ném ra lỗi để lập trình viên sửa chữa.
             * Chi tiết về exception sẽ được trình bày ở những bài học sau.
             */
            if (p1 == null || p2 == null)
            {
                throw new InvalidOperationException();
            }
            else
            {
                /*
                 * Khi dữ liệu đã ok thì ta thực hiện so sánh và trả về các giá trị 1 0 -1 tương ứng
                 * lớn hơn, bằng, bé hơn.
                 */
                if (p1.Age > p2.Age)
                {
                    return 1;
                }
                else if (p1.Age == p2.Age)
                {
                    return 0;
                }
                else
                {
                    return -1;
                }
            }
        }
    }

    public class MyArrayList : ICollection
    {
        private object[] lstObj; // mảng giá trị
        private int count; // số lượng phần tử
        private const int MAXCOUNT = 100; // số lượng phần tử tối đa

        public MyArrayList()
        {
            count = -1;
            lstObj = new object[MAXCOUNT];
        }

        public MyArrayList(int count)
        {
            this.count = count;
            lstObj = new object[count];
        }

        public MyArrayList(Array array)
        {
            array.CopyTo(lstObj, 0);
            count = array.Length;
        }

        public void CopyTo(Array array, int index)
        {
            // thực hiện copy các phần tử trong lstObj từ vị trí index đến cuối sang mảng array.
            lstObj.CopyTo(array, index);
        }

        public int Count
        {
            get { return count; }
        }

        public bool IsSynchronized
        {
            get { throw new NotImplementedException(); }
        }

        public object SyncRoot
        {
            get { throw new NotImplementedException(); }
        }

        public IEnumerator GetEnumerator()
        {
            throw new NotImplementedException();
        }
    }

}