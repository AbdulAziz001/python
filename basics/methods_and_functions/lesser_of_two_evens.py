"""
LESSER OF TWO EVENS: Write a function that returns
the lesser of two given numbers if both numbers are even,
but returns the greater, if one or both numbers are odd¶
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5
"""


def myfunc(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return b if a > b else a  # or min(a,b)
    else:
        return a if a > b else b  # or max(a,b)


# should return 10
print(myfunc(10, 20))

# should return 12
print(myfunc(7, 12))

