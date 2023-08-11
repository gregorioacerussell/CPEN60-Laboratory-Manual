# 8. Write a program that asks the user for a number of seconds and prints out how
# many minutes and seconds that is. For instance, 200 seconds is 3 minutes and 20
# seconds.

while True:
    try:
        time = int(input("Enter number of seconds: "))
        break
    except ValueError:
        print("Invalid argument.")

minutes = time//60
seconds = time%60
print(f"{time} sec = {minutes} min {seconds} sec")