# (b) One way to find out the last two digits of a number is to mod the number by
# 100. Write a program that asks the user to enter a power. Then find the last two
# digits of 2 raised to that power.

while True:
    try:
        power = int(input("Enter a power to raise to 2: "))
        break
    except ValueError:
         print("Invalid argument.")

power_value = 2**power
last_two_nb = power_value % 100
if last_two_nb < 10:
    print(f"The last digit of 2 raised to {power} is: {power_value%100}")
else:
    print(f"The last two digits of 2 raised to {power} is: {power_value%100}")
