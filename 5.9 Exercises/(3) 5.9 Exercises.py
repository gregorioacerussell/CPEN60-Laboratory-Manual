# 3. Write a program that asks the user to enter a value n, and then computes
# (1+1/2+1/3+...+1/n) - ln(n). The ln function is log in the math module.

import math

while True:
    try:
        value = int(input("Enter a value (n): "))
        break
    except ValueError:
        print("Invalid argument.")
computation = 1
for i in range(2,value+1):
    computation += 1/i
print(f"The result is: {round(computation - math.log(value), 2)}")

