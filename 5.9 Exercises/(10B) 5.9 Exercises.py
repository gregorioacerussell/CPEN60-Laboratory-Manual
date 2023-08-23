# 10. Ask the user to enter 10 test scores. Write a program to do the following:
# b.) Print out the average of the scores.

while True:
    try:
        test_scores = list(map(int, input("Enter 10 test scores: ").split()))
        if len(test_scores) == 10:
            break
        else:
            print("Please enter 10 test scores!")
    except ValueError:
        print("Invalid argument")
average = sum(test_scores) / len(test_scores)
print(f"The average score is {average}")
