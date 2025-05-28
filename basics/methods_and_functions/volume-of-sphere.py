"""Write a function that computes the volume of a sphere given its radius.

The volume of a sphere is given as

4 (pi*r**3)
_
3
"""

import math


def vol(rad):
    pi = math.pi
    remainder = 4/3
    vol_sphere = remainder*pi*(rad*rad*rad)
    return vol_sphere


print(vol(2))


