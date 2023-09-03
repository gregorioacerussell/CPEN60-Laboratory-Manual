# 22. A simple way of encrypting a message is to rearrange its characters. One way
# to rearrange the characters is to pick out the characters at even indices, put them
# first in the encrypted string, and follow them by the odd characters. For example,
# the string message would be encrypted as msaeesg because the even characters are m,
# s, a, e (at indices 0,2,4, and 6) and the odd characters are e, s, g (at indices 1, 3.
# and 5).

# a.) Write a program that asks the user for a string and uses this method to encrypt
# the string.

word = input("Enter a word to encrypt: ")
encrypt_even = []
encrypt_odd = []
for i in range(len(word)):
    if i % 2 == 0:
        encrypt_even.append(word[i])
    else:
        encrypt_odd.append(word[i])

encrypt_even.extend(encrypt_odd)
print(f"The Encrypted Message is: {''.join(map(str, encrypt_even))}")


