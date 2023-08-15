# 7 Write a program that asks the user for two numbers and prints Close if the numbers
# are within .001 of each other and Not close otherwise.

while True:
    try:
        num1 = float(input("Enter first number: "))
        break
    except ValueError:
        print("Invalid argument.")

while True:
    try:
        num2 = float(input("Enter second number: "))
        break
    except ValueError:
        print("Invalid argument.")

difference = abs(num1-num2)

if difference <= 0.001:
    print("Close")
else:
    print("Not Close")