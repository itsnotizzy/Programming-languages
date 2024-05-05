try:
  bCount = float(input('Enter initial count of bacteria: '))
  nHours = int(input('Enter the number of hours: '))

  HourToMinutes = nHours * 60
  genTime = HourToMinutes / 20
  n = 2**genTime  # Using exponentiation for bacteria growth

  print('\n')

  binaryFusion = bCount * n
  print("The number of bacteria per hour will be:")

  for x in range(1,6):  # Iterate through all hours
    value = "Hour " + str(x) + " = "
    bacteriaPerHour = x * n
    print(value + str(bacteriaPerHour))

except ValueError:
  print("Error: Please enter numbers only.")
except OverflowError:
  print("Please enter correct hours!")