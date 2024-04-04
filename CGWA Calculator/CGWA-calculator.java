import java.util.Scanner;

public class CGWAcalculator {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        double[] grades = new double[5];
        double cumulativeGWA;

        for (int i = 0; i < 5; i++) {
            System.out.print("Enter the final grade for Term " + (i + 1) + ": ");
            grades[i] = scan.nextDouble();
        }

        cumulativeGWA = (grades[0] + grades[1] + grades[2] + grades[3] + grades[4]) / 5;

        System.out.println("Cumulative GWA is: " + cumulativeGWA);
    }
}