# 16. Let L = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47].
# Use a list comprehension to produce a list of the gaps between consecutive
# entries in L. Then find the maximum gap size and the percentage of gaps that
# have size 2.

L = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

L_gaps = [ (L[i+1] - L[i]) for i in range(len(L) - 1)]
L_2 =  [i for i in L_gaps if i == 2]
L_2percentage = (len(L_2) / len(L_gaps)) * 100
print(f"The gaps of the list L are: {L_gaps}\nThe maximum gap size is: {max(L_gaps)}\nThe percentage of gaps that has size 2 is: {round(L_2percentage, 2)}%")