# 2.) Write a program that counts how many of the squares of the numbers from 1 to 100
# end in a 4 and how many end in a 9.

numbers_4 = []
numbers_9 = []
for i in range(1,100):
    squared = i**2
    last_digit = squared % 10
    if last_digit == 4:
       numbers_4.append(i)
    elif last_digit == 9:
        numbers_9.append(i)

print(f"Squares of the Numbers 1 to 100 that end in 4 are: {numbers_4}")
print(f"Squares of the Numbers 1 to 100 that end in 9 are: {numbers_9}")
