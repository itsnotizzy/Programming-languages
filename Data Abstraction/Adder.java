import java.io.PrintStream;

public class Adder {
    private int total;

    public Adder(int a) {
        this.total = a;
    }

    public Adder() {
        this(0);
    }

    public void addNum(int number) {
        this.total += number;
    }

    public int getTotal() {
        return this.total;
    }

    public static void main(String[] args) {
        Adder a = new Adder();
        a.addNum(10);
        a.addNum(20);
        a.addNum(30);
        System.out.println("Total " + a.getTotal());
    }
}