print("Enter the colors that you want to mix.", "\n")

    # Primary Colors: red, yellow, blue
def get_secondary_color(primary_color1, primary_color2):
    primary_color1 = primary_color1.lower()
    primary_color2 = primary_color2.lower()

    if (primary_color1 == "red" and primary_color2 == "blue") or (primary_color1 == "blue" and primary_color2 == "red"):
        return "Purple"
    elif (primary_color1 == "red" and primary_color2 == "yellow") or (primary_color1 == "yellow" and primary_color2 == "red"):
        return "Orange"
    elif (primary_color1 == "blue" and primary_color2 == "yellow") or (primary_color1 == "yellow" and primary_color2 == "blue"):
        return "Green"
    elif (primary_color1 == "yellow" and primary_color2 == "yellow"):
        return "Yellow"
    elif (primary_color1 == "blue" and primary_color2 == "blue"):
        return "Blue"
    elif (primary_color1 == "red" and primary_color2 == "red"):
        return "Red"
    else:
        return "Invalid combination of primary colors."

# Prompt the user to enter the primary colors
primary_color1 = input("Enter the first primary color: ")
primary_color2 = input("Enter the second primary color: ")

# Call the function to get the secondary color
secondary_color = get_secondary_color(primary_color1, primary_color2)

# Display the result to the user
print("The secondary color is:", secondary_color, "\n")