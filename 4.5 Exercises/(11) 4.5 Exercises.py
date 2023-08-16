# 11. Write a program that asks the user for an hour between 1 and 12, asks them
# to enter am or pm, and asks them how many hours into the future they want to go.
# Print out what the hour will be that many hours into the future, printing am or pm as
# appropriate.

hour = int(input("Enter hour: "))
meridiem = int(input("AM (1) or PM (2): "))
hours_ahead = int(input("How many hours ahead? "))

new_hour = hour+hours_ahead

if new_hour > 12:
    new_hour = new_hour % 12
    if new_hour == 0:
        new_hour = 12
        if meridiem == 1:
            meridiem = "PM"
        elif meridiem == 2:
            meridiem = "AM"
    elif meridiem == 1:
        meridiem = "PM"
    elif meridiem == 2:
        meridiem = "AM"
    print(f"New hour: {new_hour} {meridiem}")

elif new_hour < 12:
    if meridiem == 1:
        meridiem = "AM"
    elif meridiem == 2:
        meridiem = "PM"
    print(f"New hour: {new_hour} {meridiem}")

elif new_hour == 12:
    if meridiem == 1:
        meridiem = "PM"
    elif meridiem == 2:
        meridiem = "AM"
    print(f"New hour: {new_hour} {meridiem}")
