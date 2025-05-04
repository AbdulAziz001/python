"""
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
"""


def old_macdonald(my_string):
    if len(my_string) > 3:
        return my_string[:3].capitalize() + my_string[3:].capitalize()
    else:
        print("string is too short ")


print(old_macdonald("macdonald"))


