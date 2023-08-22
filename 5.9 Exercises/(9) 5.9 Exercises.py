# 9. Write a program to count how many integers from 1 to 1000 are not perfect squares,
# perfect cubes, or perfect fifth powers.

not_perfect_squares = []
not_perfect_cubes = []
not_perfect_fifth_power = []

for i in range(1,1001):
    sqrt = i ** (1/2)
    if sqrt != int(sqrt):
        not_perfect_squares.append(i)

for i in range(1,1001):
    sqrt = i ** (1/3)
    if sqrt != int(sqrt):
        not_perfect_cubes.append(i)

for i in range(1,1001):
    sqrt = i ** (1/5)
    if sqrt != int(sqrt):
        not_perfect_fifth_power.append(i)

print(f"Not Perfect Squares from 1 to 1000 are: {not_perfect_squares}")
print(f"Not Perfect Cubes from 1 to 1000 are: {not_perfect_cubes}")
print(f"Not Perfect Fifth Powers from 1 to 1000 are: {not_perfect_fifth_power}")