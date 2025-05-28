
def pallindrome_way1(my_string):
    rev_string = str(my_string)[::-1]
    if my_string == rev_string:
        print(f" {my_string}  is a pallindrome ")
    else:
        print(f" {my_string}  is not a pallindrome ")


def pallindrome_way2(my_string):
    rev_string = ''
    for char in my_string[::-1]:
        rev_string = rev_string + char
    if my_string == rev_string:
        print(f" {my_string}  is a pallindrome ")
    else:
        print(f" {my_string}  is not a pallindrome ")


pallindrome_way1('helleh')

pallindrome_way2('helleh')

