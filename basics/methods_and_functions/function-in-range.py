"""Write a function that checks whether a number is in a given range (inclusive of high and low)

"""


def ran_check_return_string(num, low, high):
    if low <= num <= high:
        print(f" {num} is in the range between {low} and {high}")
    else:
        print(f" {num} is not in the range between {low} and {high}")


def ran_check_return_bool(num, low, high):
    if low <= num <= high:
        return True
    else:
        return False


ran_check_return_string(5, 2, 7)

print(ran_check_return_bool(5, 2, 7))

print(ran_check_return_bool(10, 2, 7))




