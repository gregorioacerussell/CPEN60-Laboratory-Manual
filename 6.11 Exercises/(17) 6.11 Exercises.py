# 17. Write a program that generates the 26-line block of letters partially shown below.
# Use a loop containing one or two print statements.

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
            'r','s','t','u','v','w','x','y','z']

for i in range(len(alphabet)):
    for j in range(len(alphabet)):
        print(alphabet[(i + j) % len(alphabet)], end='')
    print()
