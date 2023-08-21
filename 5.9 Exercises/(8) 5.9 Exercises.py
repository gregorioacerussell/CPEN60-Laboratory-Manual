# 8. Write a program that swaps the values of three variables x, y, and z, so that x gets the value
# of y, y gets the value of z, and z gets the value of x.

while True:
    try:
        x = int(input("Enter value for x: "))
        break
    except ValueError:
        print("Invalid argument")

while True:
    try:
        y = int(input("Enter value for y: "))
        break
    except ValueError:
        print("Invalid argument")

while True:
    try:
        z = int(input("Enter value for z: "))
        break
    except ValueError:
        print("Invalid argument")

temp = x
x = y
y = z
z = temp

print("After swapping:")
print("x:", x)
print("y:", y)
print("z:", z)