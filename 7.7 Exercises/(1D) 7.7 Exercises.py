# 1. Write a program that asks the user to enter a list of integers.
# Do the following.

# d.) Print Yes if the list contains a 5 and No otherwise.

numbers = input("Enter a list of integers using spaces: ").split(' ')
has_five = False

for i in numbers:
    if i == '5':
        has_five = True

if has_five:
    print('Yes')
else:
    print('No')