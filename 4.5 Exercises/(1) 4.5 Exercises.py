# 1. Write a program that asks the user to enter a length in centimeters. If the user
# enters a negative length, the program should tell the user that the entry is invalid.
# Otherwise, the program should convert the length to inches and print out the result.
# There are 2.54 centimeters in an inch.

while True:
    try:
        cm = int(input("Enter a length in centimeters: "))
        if cm < 0:
            print("Invalid! Must be a positive number.")
            continue
        break
    except ValueError:
        print("Invalid argument")

inch = cm / 2.54
print(f"{cm} cm in inches is: {round(inch, 2)}")