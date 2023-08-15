# 9. A lot of cell phones have tip calculators. Write one. Ask the user for the price of the meal and the percent tip
# they want to leave. Then print bot the tip amount and the total bill with the tip included.
while True:
    try:
        meal_price = int(input("Input the meal price: "))
        break
    except ValueError:
        print("Please enter a number.")
while True:
    try:
        percent_tip = int(input("Input a percent tip: "))
        break
    except ValueError:
        print("Please enter a number; no need to add %.")
tip_amount = meal_price*(percent_tip*0.01)
total_bill = meal_price + tip_amount
print(f"The tip amount and total bill is {round(tip_amount, 3)} and {round(total_bill, 3)}")