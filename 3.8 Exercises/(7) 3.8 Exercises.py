# 7. Write a program that asks the user to enter an angle between -180 degrees and
# 180 degrees. Using an expression with the modulo operator, convert the angle to its
# equivalent between 0 and 360

while True:
    try:
        angle = int(input("Enter an angle: "))
        if angle >= 181:
            print("Invalid argument.")
            continue
        else:
            break
    except ValueError:
        print("Invalid argument.")

print(f"The angle is equivalent to: {angle%360}")
