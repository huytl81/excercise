using System.Threading;
using System;

namespace MultiThread
{
    //class Multi_Thread
    //{
    //    static void Main(string[] args)
    //    {
    //        DemoThread();
    //        DemoThread();
    //        DemoThread();

    //        Console.ReadLine();
    //    }

    //    static void DemoThread()
    //    {
    //        // Thực hiện vòng lặp 5 lần. Mỗi lần tốn 1 giây
    //        for (int i = 0; i < 5; i++)
    //        {
    //            // Làm gì đó tốn 1s. Dùng Thread.Sleep để luồng hiện tại ngủ theo thời gian được cài đặt.
    //            // Mục đích để giả lập độ trễ của code xử lý
    //            Thread.Sleep(TimeSpan.FromSeconds(1));
    //            Console.WriteLine(i);
    //        }
    //    }
    //}


    class MultiThread
    {
        static void Maint(string[] args)
        {
            /* Tạo một Thread t với anonymous function và gọi hàm DemoThread bên trong
             * Thread chỉ bắt đầu chạy khi gọi hàm Start
             * Bạn có thể thực hiện một hàm hay nhiều dòng code ở bên trong anonymous function này
             */
            //Thread t = new Thread(() => {
            //    DemoThread("Thread 1");
            //});
            //t.Start();

            //Thread t2 = new Thread(() => {
            //    DemoThread("Thread 2");
            //});
            //t2.Start();

            //Thread t3 = new Thread(() => {
            //    DemoThread("Thread 3");
            //});
            //t3.Start();

            for (int i = 0; i < 5; i++)
            {
                int j = i;
                Thread t = new Thread(() => {
                    DemoThread("Thread " + j);
                });
                t.Start();
            }

            Console.ReadLine();
        }

        static void DemoThread(string threadIndex)
        {
            // Thực hiện vòng lặp 5 lần. Mỗi lần tốn 1 giây
            for (int i = 0; i < 100; i++)
            {
                // Làm gì đó tốn 1s. Dùng Thread.Sleep để luồng hiện tại ngủ theo thời gian được cài đặt.
                // Mục đích để giả lập độ trễ của code xử lý
                //Thread.Sleep(TimeSpan.FromSeconds(1));

                Console.WriteLine(threadIndex + " - " + i);
            }
        }
    }


}