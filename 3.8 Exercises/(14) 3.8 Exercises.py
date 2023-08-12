# Write a program that asks the user to enter an angle in degrees and prints out
# the sine of that angle.

import math
while True:
    try:
        angle = int(input("Enter an angle: "))
        break
    except ValueError:
        print("Invalid argument")

radian = math.radians(angle)
print(f"The sin of the angle {angle} is: {math.sin(radian)} ")
