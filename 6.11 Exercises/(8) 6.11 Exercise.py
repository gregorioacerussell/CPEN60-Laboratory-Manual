# 8. At a certain school, student email addresses end with @student.college.edu, while
# professor email addresses end with @prof.college.edu. Write a program that first asks
# the user how many email addresses are entered, the program should print out a message
# indicating either that all the addresses are student addresses or that were some
# professor addresses entered.
while True:
    try:
        num = int(input("How many email addresses will be entered?: "))
        break
    except ValueError:
        print("Invalid argument")
while True:
    emails = input(f"Enter the {num} emails (Use spaces per email): ").split()
    if len(emails) != num:
        print(f"Please input {num} emails")
    else:
        break

students = 0
professors = 0
for i in emails:
    if "@student.college.edu" in i:
        students += 1
    elif "@prof.college.edu" in i:
        professors += 1

print(f"There were {students} student emails inputted and {professors} professor emails inputted.")
