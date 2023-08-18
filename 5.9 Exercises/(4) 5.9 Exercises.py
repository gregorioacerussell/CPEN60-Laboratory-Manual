# 4. Write a program that compute the sum 1 - 2 + 3 - 4 + ... + 1999 - 2000

total = 0
for i in range(1,2001):
    if i % 2 == 0:
        total -= i
    else:
        total += i
print(f"The sum is: {total}")
