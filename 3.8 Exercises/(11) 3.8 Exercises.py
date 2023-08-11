# 11. Write a program that asks the user to enter a weight in kilograms. The program
# should convert it to pounds, printing the answer rounded to the nearest tenth of a
# pound.

while True:
    try:
        kilograms = int(input("Enter your weight in kilograms: "))
        break
    except ValueError:
        print("Invalid argument.")

pounds = kilograms * 2.205
print(f"Your weight in pounds (lbs) is: {round(pounds, 1)}")
