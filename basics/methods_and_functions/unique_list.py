"""
Write a Python function that takes a list and returns a new list with unique elements of the first list.
"""
def unique_list(my_list):
    unique_list_to_return = []
    for item in my_list:
        if item not in unique_list_to_return:
            unique_list_to_return.append(item)
        else:
            pass
    print(unique_list_to_return)


unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])

