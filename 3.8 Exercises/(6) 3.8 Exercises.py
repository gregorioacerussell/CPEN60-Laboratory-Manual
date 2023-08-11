# 6. Write a program that asks the user to enter two numbers, x and y, and computes...

while True:
    try:
        x = int(input("Enter value for x: "))
        break
    except ValueError:
        print("Invalid argument.")
while True:
    try:
        y = int(input("Enter value for y: "))
        break
    except ValueError:
        print("Invalid argument.")
calculation = (abs(x-y))/(x+y)
print(f"The value you got based on the calculation is: {round(calculation, 2)}")
