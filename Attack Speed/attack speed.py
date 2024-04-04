print("Enter numbers only for base and level, and a number (with or without '%') for bonus attack speed (e.g., 4 or 4%).", "\n")

def calculate_attack_speed(base_attack_speed, bonus_attack_speed_input, level):
  """Calculates the character's attack speed at a certain level.

  Args:
      base_attack_speed: The character's base attack speed (float).
      bonus_attack_speed_input: The bonus attack speed as a number (with or without '%').
      level: The character's level (integer).

  Returns:
      The character's current attack speed rounded to three decimal places (float).
  """

  # Check if bonus attack speed includes '%' sign
  if bonus_attack_speed_input.endswith('%'):
    # Extract bonus attack speed value (remove '%')
    bonus_attack_speed_percent = int(bonus_attack_speed_input[:-1])
  else:
    # Assume value is entered without '%'
    bonus_attack_speed_percent = int(bonus_attack_speed_input)

  # Convert bonus attack speed to decimal before calculation
  bonus_attack_speed_decimal = bonus_attack_speed_percent / 100
  current_attack_speed = base_attack_speed * (1 + (bonus_attack_speed_decimal * (level - 1)))
  return round(current_attack_speed, 3)

# Get user input with error handling
while True:
  try:
    base_attack_speed = float(input("Enter the base attack speed: "))
    bonus_attack_speed_input = input("Enter the bonus attack speed %: ")
    level = int(input("Enter the level: "))
    break  # Exit loop if all inputs are valid
  except ValueError:
    print("Invalid input. Please enter numbers only for base and level, and a number (with or without '%') for bonus attack speed (e.g., 4 or 4%).")

# Calculate and display attack speed
current_attack_speed = calculate_attack_speed(base_attack_speed, bonus_attack_speed_input, level)
print(f"The character's current attack speed is {current_attack_speed:.3f}.", "\n")