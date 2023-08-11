# 14. User for loops to print a diamond like the one below. Allow the user to
# specify how high the diamond should be.
while True:
    try:
        height = int(input("Enter height of diamond: "))
        break
    except ValueError:
        print("Invalid argument.")

for i in range(height):
    print(" "*(height-i-1) + " *"*(i+1))
for j in range(height):
    print(" "*(j+1) + " *"*(height-j-1))