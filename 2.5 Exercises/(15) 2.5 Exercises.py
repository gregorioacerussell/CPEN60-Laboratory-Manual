# 15. Write a program that prints a giant letter A like the one below. Allow
# the user to specify how large the letter should be.

while True:
    try:
        height = int(input("Enter height of letter A: "))
        break
    except ValueError:
        print("Invalid argument.")

for i in range(height):
    print(" "*(height-i) + "*")

# Not Completely Finished