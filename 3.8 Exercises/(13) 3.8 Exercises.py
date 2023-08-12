# 13. Write a program that asks the user for a number and then prints out the
# sine, cosine, and tangent of that number.

import math
while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid argument.")

print(f"Value: {number}")
print(f"Sine (Radian): {round(math.sin(number), 2)}")
print(f"Cosine (Radian): {round(math.cos(number), 2)}")
print(f"Tan (Radian): {round(math.tan(number), 2)}")