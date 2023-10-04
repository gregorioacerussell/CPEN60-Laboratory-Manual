# 19. Write a program that creates and prints an 8x8 list whose entries
# alternate between 1 and 2 in a checkerboard pattern, starting with 1 in
# the upper left corner.

import numpy as np
sample_list = np.ones((8,8), dtype=int)
sample_list[1::2, ::2] = 2
sample_list[::2, 1::2] = 2
print(sample_list)