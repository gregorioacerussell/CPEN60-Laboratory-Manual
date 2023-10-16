# 8. The GCD of two numbers is the largest number that both are divisible by.
# For instance, gcd(18,42) is 6 because the largest number that both 18 and 42
# are divisible by is 6. Write a program that asks the user for two numbers and
# computes their gcd. Shown below is a way to compute the GCD, called Euclid's
# Algorithm

# First compute the remainder of dividing the largest number by the smallest number.
# Next, replace the largest number with the smaller number and smaller number with the remainder.
# Repeat this process until the smaller number is 0. The GCD is the last value of the larger number.

def input_validation(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Input a number.")

num1 = input_validation("Enter first number: ")
num2 = input_validation("Enter second number: ")
larger_number = max(num1, num2)
smaller_number = min(num1, num2)
remainder = 0

while smaller_number > 0:
    remainder = larger_number % smaller_number
    larger_number = smaller_number
    smaller_number = remainder

print(f"""
The GCD of {num1} and {num2} is {larger_number}.""")

