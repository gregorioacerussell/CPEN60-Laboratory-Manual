# 18. Write a program that given an amount of change less than
# $1.00 will print out exactly how many quarters, dimes, nickels, and
# pennies will be needed to efficiently make that change.

while True:
    try:
        money = float(input("Enter money less than 1: "))
        if money >= 1:
            print("Must be less than 1.")
            continue
        elif money < 0:
            print("Must be a positive amount.")
            continue
        else:
            break
    except ValueError:
        print("Invalid argument")

cents = money*100

quarter = cents // 25
quarter_change = cents % 25

dime = quarter_change // 10
dime_change = quarter_change % 10

nickel = dime_change // 5
nickel_change = dime_change % 5

penny = nickel_change

print()
print(f"${money} is equivalent to:")
print()
print(f"Quarters: {int(quarter)}")
print(f"Dimes: {int(dime)}")
print(f"Nickels: {int(nickel)}")
print(f"Pennies: {int(penny)}")
