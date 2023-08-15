# 4. Write a program that asks the user how many credits they have taken.
# If they have taken 23 or less, print that the student is a freshman. If they
# have taken between 24 and 53, print that they are a sophomore. The range for
# juniors is 54 to 83, and for seniors it is 84 and over.

while True:
    try:
        credit = int(input("Enter credits: "))
        if 0 < credit <= 23:
            print("You are a freshman student.")
            break
        elif 24 <= credit <= 53:
            print("You are a sophomore student.")
            break
        elif 54 <= credit <= 83:
            print("You are a junior student.")
            break
        elif credit >= 84:
            print("You are a senior student.")
            break
        else:
            print("Invalid credit.")
            continue
    except ValueError:
        print("Invalid argument")