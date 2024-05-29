using System;
using System.Threading;

class Program
{
    static ManualResetEvent manualResetEvent = new ManualResetEvent(false);

    static void Main()
    {
        Thread thread = new Thread(DoWork); // Create the thread object

        thread.Start();
        Thread.Sleep(2000);
        manualResetEvent.Reset(); // Suspend the thread
        Console.WriteLine("Thread is suspended...");
        Thread.Sleep(2000);
        manualResetEvent.Set(); // Resume the thread
        Console.WriteLine("Thread is resumed...");
        thread.Join();
    }

    static void DoWork()
    {
        Console.WriteLine("Thread is doing some work...");

        manualResetEvent.WaitOne(); // Wait until the ManualResetEvent is set
        Console.WriteLine("Thread is continuing its work...");
    }
}