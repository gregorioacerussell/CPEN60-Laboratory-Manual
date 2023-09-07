# 1. Write a program that asks the user to enter a list of integers.
# Do the following.

# f.) Remove the first and last items from the list, sort the remaining items,
# and print the result.

numbers = input("Enter a list of integers using spaces: ").split(' ')
numbers.remove(numbers[0])
numbers.remove(numbers[len(numbers)-1])
numbers.sort()
print(numbers)