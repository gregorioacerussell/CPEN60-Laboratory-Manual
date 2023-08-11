# 9. Print out the fibonacci sequence.
while True:
    try:
        sequence = int(input("Enter a sequence of Fibonacci: "))
        a = 1
        b = 1
        numbers = [a, b]
        for i in range(2, sequence):
            c = a + b
            a = b
            b = c
            numbers.append(c)
        print(numbers)
        break
    except ValueError:
        print("Input valid argument.")