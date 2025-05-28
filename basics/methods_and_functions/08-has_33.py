"""
Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False

"""


def has_33(my_list):
    second_item = my_list[1]
    for item in my_list:
        if item == 3 and second_item == 3:
            return True
        second_item = item
    return False


my_list = [1, 2, 3]
print(has_33(my_list))  # False

my_list = [1, 3, 3]
print(has_33(my_list))  # True

my_list = [3, 1, 3]
print(has_33(my_list))  # False

