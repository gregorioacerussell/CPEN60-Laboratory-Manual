# 9. Write a program that asks the user for an hour between 1 and 12 and for how
# many hours in the future they want to go. Print out what the hour will be that
# many hours into the future.

while True:
    try:
        hour = int(input("Enter hour: "))
        break
    except ValueError:
        print("Invalid argument.")
while True:
    try:
        hours_ahead = int(input("How many hours ahead? "))
        break
    except ValueError:
        print("Invalid argument.")

hour_total = hour + hours_ahead
if hour_total == 12 or hour_total < 12:
    print(f"New hour: {hour_total} o'clock")
elif hour_total > 12:
    print(f"New hour: {hour_total - 12} o'clock")