# Ask the user to enter a temperature in Celsius. The program should print a
# message based on the temperature:

while True:
    try:
        temp = float(input("Enter a temperature in Celsius: "))
        if temp < -273.15:
            print("Invalid temperature")
            continue
        elif temp == -273.15:
            print("Temperature is absolute 0.")
            break
        elif - 273.15 < temp < 0:
            print("Temperature is below freezing.")
            break
        elif 0 < temp < 100:
            print("Temperature is in normal range.")
            break
        elif temp == 100:
            print("Temperature is at boiling point.")
            break
        elif temp > 100:
            print("Temperature is above boiling point!")
            break
        elif temp == 0:
            print("Temperature is at freezing point.")
            break
    except ValueError:
        print("Invalid argument.")


