# 13. Let L be a list of strings. Write a list comprehensions that create new lists from L for each of the
# following. 

# (a) A list that consists of the strings of s with their first characters removed.

L = ['science', 'sets', 'sabotage', 'shrek', 'show']
L_tampered = [i[1:] for i in L]
print(L_tampered)