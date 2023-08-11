# 12. Use a for loop to print a triangle like the one below. Allow the user to specify how
# high the triangle should be.

while True:
    try:
        height = int(input("Enter height of triangle: "))
        break
    except ValueError:
        print("Invalid argument.")

for i in range(height):
    for j in range(i+1):
        print("*",end='')
    print()