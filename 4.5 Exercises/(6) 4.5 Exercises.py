# 6. A store charges $12 per item if you buy less than 10 items. If you buy
# between 10 and 99 items, the cost is $10 per item. If you buy 100 or more items,
# the cost is $7 per item. Write a program that asks the user how many items they are
# buying and prints the total cost.

while True:
    try:
        items = int(input("Enter how many items you bought: "))
        if items < 10:
            cost = 12
            print(f"The total cost for {items} items is: ${items*cost}.")
            break
        elif 10 <= items <= 99:
            cost = 10
            print(f"The total cost for {items} items is: ${items*cost}.")
            break
        elif items >= 100:
            cost = 7
            print(f"The total cost for {items} items is ${items*cost}")
            break
    except ValueError:
        print("Invalid argument.")