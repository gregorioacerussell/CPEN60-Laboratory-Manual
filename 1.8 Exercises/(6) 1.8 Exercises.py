# 6. Ask the user to enter a number x. Use the sep optional argument to print out x, 2x, 3x, 4x, and 5x,
# each separated by three dashes, like below.
number = int(input("Enter a number: "))
print(number, number*2, number*3, number*4, number*5, sep="---")