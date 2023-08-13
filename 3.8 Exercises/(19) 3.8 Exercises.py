# 19. Write a program that draws "modular rectangles" like the ones below.
# The user specifies the width and height of the rectangle, and the entries
# start at 0 and increase typewriter fashion from left to right and top to
# bottom, but are all done mod 10.

width = int(input("Enter width: "))
height = int(input("Enter height: "))

for i in range(height):
    for j in range(width):
        print((i*width+j) % 10, end= ' ')
    print()