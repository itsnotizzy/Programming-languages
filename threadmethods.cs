using System;
using System.Threading;

// EXTRA SAMPLE ONLY !!!

class Program
{
    static void Main()
    {
        Thread thread = new Thread(DoWork);

        thread.Start();
        Thread.Sleep(2000);
        thread.Join();
    }

    static void DoWork()
    {
        Console.WriteLine("Thread is doing some work...");
    }
}
