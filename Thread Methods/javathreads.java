public class ThreadMethods {

    public static void main(String[] args) {
        Thread thread = new Thread(() -> System.out.println("Thread is running"));
        thread.start();

        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        boolean isAlive = thread.isAlive();
        System.out.println("Thread is alive: " + isAlive);

        try {
            thread.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        Thread currentThread = Thread.currentThread();
        System.out.println("Current thread: " + currentThread.getName());

        thread.setPriority(Thread.MAX_PRIORITY);
        int priority = thread.getPriority();
        System.out.println("Thread priority: " + priority);

        Thread.yield();

        thread.interrupt();
        boolean isInterrupted = thread.isInterrupted();
        System.out.println("Thread is interrupted: " + isInterrupted);
    }
}