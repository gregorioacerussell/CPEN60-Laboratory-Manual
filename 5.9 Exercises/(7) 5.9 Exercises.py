# An integer is called squarefree if it is not divisible by any perfect squares other than 1. For
# instance, 42 is squarefree because its divisors are 1, 2, 3, 6, 7, 21, and 42, and none of those
# numbers (except 1) is a perfect square. On the other hand, 45 is not squarefree because it is
# divisible by 9, which is a perfect square. Write a program that asks the user for an integer and
# tells them if it is squarefree or not.

while True:
    try:
        num = int(input("Enter an integer: "))
        break
    except ValueError:
        print("Invalid argument.")

divisors = []
for i in range(1,num):
    if num % i == 0:
        divisors.append(i)

is_square_free = True
for i in range(1, len(divisors)):
    sqrt = divisors[i] ** (0.5)
    if sqrt.is_integer():
        is_square_free = False
        break
if is_square_free:
    print(f"{num} is a squarefree integer.")
else:
    print(f"{num} is not a squarefree integer.")


