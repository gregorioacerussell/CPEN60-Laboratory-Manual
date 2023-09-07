# 1. Write a program that asks the user to enter a list of integers.
# Do the following.

# c.) Print the list in reverse order.

numbers = input("Enter a list of integers using spaces: ").split(' ')
print(f"The list in reversed order is: {' '.join(numbers[::-1])}")