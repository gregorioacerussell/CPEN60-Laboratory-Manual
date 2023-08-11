# (c) Write a program that asks the user to enter a power and how many digits they
# want. Find the last that many digits of 2 raised to the power the user entered.

while True:
    try:
        power = int(input("Enter a power to raise to 2: "))
        break
    except ValueError:
        print("Invalid argument")
while True:
    try:
        last_digit_count = int(input("Enter how many digits you want it to print out: "))
        break
    except ValueError:
        print("Invalid argument")

power_value = 2**power
last_digit_value = 10

for i in range(1, last_digit_count):
    last_digit_value *= 10

result = power_value % last_digit_value
print(f"The last {last_digit_count} digits of 2 raised to {power} is: {result:0{last_digit_count}}")
