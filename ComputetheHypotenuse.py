#function = l of 2 shorter sides as ()
#return hypotenuse using pythag
#program = read l of 2 from user, display result
from math import sqrt
def sides(a,b):
    c = sqrt((a**2) + (b**2))
    return (c)
print (sides(float(input()),float(input())),'units')