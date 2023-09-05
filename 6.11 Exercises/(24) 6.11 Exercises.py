# 24. In calculus, the derivative of x^4 is 4x^3. Write a program that
# asks the user for input like x^3 or x^25 and prints the derivative.

value = input("Enter a value to derivative ex: (x^3): ").split('^')
print(f"{value[1]}{value[0]}^{int(value[1])-1}")

