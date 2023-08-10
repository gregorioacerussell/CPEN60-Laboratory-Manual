# 7. Write a program that asks the user for a weight in kilograms and converts it to pounds. There are 2.2 pounds in
# a kilogram.
while True:
    try:
        kg = int(input("Enter your weight in kilograms: "))
        lbs = kg*2.2
        break
    except ValueError:
        print("Please input a number.")
print(f"Your weight in pounds is {int(lbs)} lbs.")