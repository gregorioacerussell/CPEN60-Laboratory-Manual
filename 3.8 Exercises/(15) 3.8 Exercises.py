# Write a program that prints out the sine and cosine of the angles ranging from
# 0 to 345 degrees in 15 degree increments. Each result should be rounded to 4
# decimal places.

import math

for i in range(0, 345, 15):
    radian = math.radians(i)
    sine = math.sin(radian)
    cosine = math.cos(radian)
    print(f"{i} --- {round(sine, 4)}  {round(cosine, 4)}")