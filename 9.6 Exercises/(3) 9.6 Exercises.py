# A good program will make sure that the data its user enter is valid.
# Write a program that asks the user for a weight and converts it from kilograms
# to pounds. Whenever the user enters a weight below 0, the program should tell
# them that their entry is invalid and then ask them again to enter a weight.
# [Hint: Use a while loop, not an if statement].

while True:
    try:
        weight_kg = int(input("Enter a weight in kilogram: "))
        if weight_kg < 0:
            print("Please input an integer above 0.")
            continue
        else:
            print(f"{weight_kg} kg in pounds is {str(round(weight_kg*2.2, 2))} lbs.")
            break
    except ValueError:
        print("Please input an integer.")
        continue
