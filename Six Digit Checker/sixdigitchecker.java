import java.util.Scanner;

public class SixDigitChecker {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a 6-digit number: ");
        int number = scanner.nextInt();

        // Check if the number is 6 digits long
        if (number < 100000 || number > 999999) {
            System.out.println("Invalid input: Please enter a 6-digit number.");
            return;
        }

        // Extract the last digit
        int lastDigit = number % 10;

        // Remove the last digit by integer division
        int fiveDigitNumber = number / 10;

        // Calculate the remainder of dividing the 5-digit number by 7
        int remainder = fiveDigitNumber % 7;

        // Check if the remainder is equal to the last digit
        boolean isMatch = remainder == lastDigit;

        System.out.println(isMatch);
    }
}