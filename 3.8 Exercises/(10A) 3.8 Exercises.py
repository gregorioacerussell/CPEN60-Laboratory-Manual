# 10.) (a) One way to find out the last digit of a number is to mod the number by
# 10. Write a program that asks the user to enter a power. Then find the last digit
# of 2 raised to that power.

while True:
    try:
        power = int(input("Enter a power to raise to 2: "))
        break
    except ValueError:
         print("Invalid argument.")

power_value = 2**power
print(f"The last digit of 2 raised to {power} is: {power_value%10}")
