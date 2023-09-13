# 8. Write a program that asks the user for an integer and creates a list
# that consists of the factors of that integers.

while True:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("Please enter a number")
num_factors = [i for i in range(1, num+1) if num % i == 0]
print(f"The factors of {num} are: {', '.join(map(str, num_factors))}")