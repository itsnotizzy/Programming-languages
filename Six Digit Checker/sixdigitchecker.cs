using System;

public class Program
{
    public static void Main()
    {
        try
        {
            Console.Write("Enter a 6-digit number: ");
            int number = int.Parse(Console.ReadLine());

            // Check if the number is 6 digits long
            if (number < 100000 || number > 999999)
            {
                Console.WriteLine("Invalid input: Please enter a 6-digit number.");
                return;
            }

            // Extract the last digit
            int lastDigit = number % 10;

            // Remove the last digit by integer division
            int fiveDigitNumber = number / 10;

            // Calculate the remainder of dividing the 5-digit number by 7
            int remainder = fiveDigitNumber % 7;

            // Check if the remainder is equal to the last digit
            bool isMatch = remainder == lastDigit;

            Console.WriteLine(isMatch);
        }
        catch (FormatException)
        {
            Console.WriteLine("Invalid input: Please enter a 6-digit number.");
        }
    }
}
