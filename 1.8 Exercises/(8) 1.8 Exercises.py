# 8. Write a program that asks the user to enter three numbers (use three separate input statements). Create
# variables called total and average that hold the sum and average of the three numbers and print out the value of
# total and average.
numbers = []
for i in range(3):
    while True:
        try:
            num = int(input(f"Enter number {1+i}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Please input a number.")
total = sum(numbers)
average = total/(len(numbers))
print(f"The total and average of {numbers} are {total} and {int(average)}")