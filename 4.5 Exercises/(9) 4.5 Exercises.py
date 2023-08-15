# 9. Write a program that asks the user to enter a number and prints out all the
# divisors of that number.

while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid argument.")

divisors = []

for i in range(1, number+1):
    if number % i == 0:
        divisors.append(i)
print(f"The divisors of {number} are: {divisors}")
