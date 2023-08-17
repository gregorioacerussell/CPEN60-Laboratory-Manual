# 1. Write a program that counts how many of the squares of the numbers from 1 to
# 100 end in a 1.

square = 0
numbers = []
for i in range(1,100):
    square = i**2
    last_digit = square % 10
    if last_digit == 1:
        numbers.append(i)

print(f"The squares of the numbers from 1 to 100 that ends in a 1 are: {numbers}")
