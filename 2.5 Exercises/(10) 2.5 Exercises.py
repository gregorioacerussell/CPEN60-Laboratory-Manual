# 10. Use a for loop to print a box like the one below. Allow the user to specify how wide and how high the box
# should be.
while True:
    try:
        height = int(input("Enter height of box: "))
        break
    except ValueError:
        print("Input a valid argument.")
while True:
    try:
        width = int(input("Enter width of box: "))
        break
    except ValueError:
        print("Input a valid argument.")
for i in range(height):
    print('*'*width)