"""
Write a Python function to multiply all the numbers in a list.

"""
def multiply(my_list):
    final_value = 1
    for item in my_list:
        final_value = final_value * item

    return final_value


print(multiply([1, 2, 3, -4]))

