# 8.) A year is a leap year if it is divisible by 4, except that years divisible by 100
# are not leap years unless they are also divided by 400. Write a program that asks the
# for a year and prints out whether it is a leap year or not.

while True:
    try:
        year = int(input("Enter a year: "))
        if year % 4 == 0:
            print("Leap Year!")
            break
        elif year % 100 == 0:
            print("Not a Leap Year")
            break
        elif year % 400 == 0:
            print("Leap Year!")
            break
        else:
            print("Not a Leap Year")
            break
    except ValueError:
        print("Invalid argument.")

