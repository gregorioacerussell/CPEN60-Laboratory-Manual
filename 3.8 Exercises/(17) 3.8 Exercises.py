# 17. A year is leap year if it divisible by 4, except that years divisible by 100
# are not leap years unless they are also divisible by 400. Ask the user to enter a
# year, and, using the // operator, determine how many leap years there have been
# between 1600 and that year.

while True:
    try:
        year = int(input("Enter a year: "))
        break
    except ValueError:
        print("Invalid argument.")

leap_years = 0

for i in range(1600, year):
    if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):
        leap_years += 1

print(f"There have been {leap_years} leap years in 1600 up to {year}")

