# 1. Write a program that asks the user to enter a list of integers.
# Do the following.

# e.) Print the number of fives in the list.

numbers = input("Enter a list of integers using spaces: ").split(' ')
five_counter = 0
for i in numbers:
    if i == '5':
        five_counter += 1
print(f"There are {five_counter} fives in the list inputted.")