# 10. Ask the user to enter 10 test scores. Write a program to do the following:
# a.) Print out the highest and lowest scores.

while True:
    try:
        test_scores = list(map(int, input("Enter 10 test scores: ").split()))
        if len(test_scores) == 10:
            break
        else:
            print("Please enter 10 test scores!")
    except ValueError:
        print("Invalid argument")
print(f"The highest score is {max(test_scores)} while the lowest is {min(test_scores)}.")
