# 8. Write a program that asks the user for their name and how many times to print it. The program should print out
# the user's name the specified number of times.
while True:
    name = input("Please enter your first name: ")
    if name.isdigit():
        print("Input a valid argument.")
        continue
    else:
        break
while True:
    try:
        repetition = int(input("How many times do you want it to print out?: "))
        break
    except ValueError:
        print("Input a valid argument.")
for i in range(repetition):
    print(name)