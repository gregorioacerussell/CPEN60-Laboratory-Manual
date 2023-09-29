# 13. Let L be a list of strings. Write list comprehensions that create new lists
# from L for each of the following.

# (b) A list of the lenghts of the string of s.

L = ['science', 'sets', 'sabotage', 'shrek', 'show', 'se', 'sa', 'so', 'su']
L_length = [i for i in L if len(i) >= 3]
print(L_length)
