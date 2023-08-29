# 9. Ask the user for a number and then print the following, where the pattern ends
# at the number that the user enters.

while True:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid argument")

for i in range(num):
     print(" "*i, i+1)
