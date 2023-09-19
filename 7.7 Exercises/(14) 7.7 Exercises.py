# 14. Write a program that asks the user to enter a length in feet. The program should
# then give the user the option to convert from feet into inches, yards, miles,
# millimeters, centimeters, meters or kilometers. Say if the user enters a 1, then the
# program converts to inches, if they enter a 2, then the program converts to yards, etc.
# while this can be done with if statements, it is much shorter with lists and it is also
# easier to add new conversions if you use lists.

while True:
    try:
        feet = int(input("Enter length in feet: "))
        break
    except ValueError:
        print("Please enter an integer.")
        continue

print("""         Enter 1 to convert to inches, 
         Enter 2 to convert to yards,
         Enter 3 to convert to miles,
         Enter 4 to convert to millimeters,
         Enter 5 to convert to centimeters,
         Enter 6 to convert to meters,
         Enter 7 to convert to kilometers""")
choice = int(input(": "))

# conversion
inches = feet * 12
yards = feet * 0.33333
miles = feet * 0.000189393939
millimeters = feet * 304.8
centimeters = feet * 30.48
meters = feet * 0.3048
kilometers = feet * 0.0003048

conversion = [inches, yards, miles, millimeters, centimeters, meters, kilometers]

# output
print(conversion[choice-1])

