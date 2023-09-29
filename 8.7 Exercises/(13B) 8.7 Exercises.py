# 13. Let L be a list of strings. Write list comprehensions that create new lists
# from L for each of the following.

# (b) A list of the lenghts of the string of s.

L = ['science', 'sets', 'sabotage', 'shrek', 'show']
L_length = [len(i) for i in L]
print(L_length)
