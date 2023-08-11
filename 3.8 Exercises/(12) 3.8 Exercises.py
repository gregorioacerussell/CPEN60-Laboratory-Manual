# 12. Write a program that asks the user for a number and prints out the factorial of
# that number.

number = int(input("Enter a number: "))
value = 1
for i in range(number):
    value *= i+1
print(f"{number}! is equivalent to: {value}")
