# 16. Below is described how to find the date of Easter in any year. Despite
# its intimidating appearance, this is not a hard problem. Note that [x] is the
# floor function, which for positive numbers just drops the decimal part of the
# number. For instance [3.14] = 3. The floor function is part of the math module.

# Easter is either March (22+d +e) or April (d +e−9). There is an exception if d = 29 and e = 6.
# In this case, Easter falls one week earlier on April 19. There is another exception if d = 28,
# e = 6, and m = 2, 5, 10, 13, 16, 21, 24, or 39. In this case, Easter falls one week earlier on April
# 18. Write a program that asks the user to enter a year and prints out the date of Easter in that
# year.

while True:
    try:
        year = int(input("Enter a year: "))
        break
    except ValueError:
        print("Invalid argument")

C = (year - 1) // 100
Y = year
m = (15 + C - (C//4) - ((8*C) + 13)/25) % 30
n = (4 + C - (C//4)) % 7
a = Y % 4
b = Y % 7
c = Y % 19
d = (19*c + m) % 30
e = (2*a + 4*b + 6*d + n) % 7

if d == 29 and e == 6:
    print("Easter is on April 19")
elif d == 28 and e == 6 and m in (2, 5, 10, 13, 16, 21, 24, 39):
    print("Easter is on April 18")
else:
    if (22 + d + e) > 31:
        april_day = int(d+e-9)
        if april_day == 0:
            print(f"Easter is on March {int(22 + d + e)}")
        else:
            print(f"Easter is on April {april_day}")
    else:
        print(f"Easter is on March {int(22+d+e)}")