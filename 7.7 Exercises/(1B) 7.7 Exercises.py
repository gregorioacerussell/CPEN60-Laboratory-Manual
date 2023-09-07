# 1. Write a program that asks the user to enter a list of integers.
# Do the following.

# b.) Print the last item in the list.

numbers = input("Enter a list of integers using spaces: ").split(' ')
print(f"The last item in the list is {numbers[len(numbers)-1]}.")