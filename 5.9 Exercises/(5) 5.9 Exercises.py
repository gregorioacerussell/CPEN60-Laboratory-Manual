# 5. Write a program that asks the user to enter a number and prints the sum of
# the divisors of that number. The sum of the divisors of a number is an
# important function in number theory.

divisors = []

while True:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid argument")

for i in range(1, num+1):
    if num % i == 0:
        divisors.append(i)

print(f"The sum of the divisors of {num} is: {sum(divisors)}")