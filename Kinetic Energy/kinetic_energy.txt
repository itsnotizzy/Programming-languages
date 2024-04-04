print("Enter valid numbers only for mass and velocity.", "\n")

def kinetic_energy(mass, velocity):
  """Calculates the kinetic energy of an object.

  Args:
      mass: The mass of the object in kilograms.
      velocity: The velocity of the object in meters per second.

  Returns:
      The kinetic energy of the object in joules, or a message indicating an error.
  """

  try:
    return 0.5 * mass * velocity**2
  except ValueError:
    return "Error: Please enter valid numbers only for mass and velocity."

# Usage
while True:
  try:
    mass = float(input("Enter mass in kilograms: "))
    velocity = float(input("Enter velocity in meters per second: "))
    break  # Exit the loop if valid numbers are entered
  except ValueError:
    print("Error: Please enter valid numbers only for mass and velocity.")

kinetic_energy_joules = kinetic_energy(mass, velocity)

print(f"The object's kinetic energy is: {kinetic_energy_joules:.2f} J.", "\n")