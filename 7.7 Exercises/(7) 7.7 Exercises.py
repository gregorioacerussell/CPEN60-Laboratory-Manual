# 7. Write a program that takes any two lists L and M of the same size and adds their
# elements together to form a new list N whose elements are sums of the corresponding
# elements in L and M. For instance, if L = [3,1,4] and M = [1,5,9], then N should equal
# [4,6,13]

M = input("Enter 3 values (ex: 1, 3, 5): ").split(', ')
N = input("Enter another 3 different values: ").split(', ')
L = []

for i in range(len(M)):
    L.append(int(M[i]) + int(N[i]))
print(L)
