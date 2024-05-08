def main():
    try:
        number = int(input("Enter a 6-digit number: "))
    except ValueError:
        print("Invalid input: Please enter a 6-digit number.")
        return

    # Check if the number is 6 digits long
    if number < 100000 or number > 999999:
        print("Invalid input: Please enter a 6-digit number.")
        return

    # Extract the last digit
    last_digit = number % 10

    # Remove the last digit by integer division
    five_digit_number = number // 10

    # Calculate the remainder of dividing the 5-digit number by 7
    remainder = five_digit_number % 7

    # Check if the remainder is equal to the last digit
    is_match = remainder == last_digit

    print(is_match)

if __name__ == "__main__":
    main()