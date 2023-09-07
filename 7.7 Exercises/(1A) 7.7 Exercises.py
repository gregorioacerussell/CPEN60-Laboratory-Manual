# 1. Write a program that asks the user to enter a list of integers.
# Do the following.

# a.) Print the total number of items in the list.

numbers = input("Enter a list of integers using spaces: ").split(' ')
print(f"The total number of items in the list are {len(numbers)}.")