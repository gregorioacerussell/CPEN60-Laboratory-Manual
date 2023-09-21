# 2. Write a program that allows the user to enter five numbers (read as strings).
# Create a string that consists of the user's number separated by plus signs. For
# instance, if the user enters 2, 5, 11, 33, and 55, then the string should be
# '2+5+11+33+55'.

numbers = input("Enter five numbers in this format (1, 2, 3, 4, 5): ").split(', ')
print('+'.join(map(str, numbers)))