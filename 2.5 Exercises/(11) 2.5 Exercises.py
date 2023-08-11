# 11. Use a for loop to print a box like the one below. Allow the user to specify how wide
# and how high the box should be.

while True:
    try:
        height = int(input("Enter height of box: "))
        break
    except ValueError:
        print("Invalid argument.")
while True:
    try:
        width = int(input("Enter width of box: "))
        break
    except ValueError:
        print("Invalid argument.")

for i in range(width): # top of box
    print("*", end='')
print()
for i in range(height-2): # height/gap of box
    print("*", end='')
    print(" "*(width-2), end='')
    print("*")
for i in range(width): # bot of box
    print("*", end='')
print()