'''skyline'''

'''Define a function called myfunc that takes in a string, and returns a matching string 
where every even letter is uppercase, and every odd letter is lowercase. Assume that the incoming 
string only contains letters, and don't worry about numbers, spaces or punctuation. The output string 
can start with either an uppercase or lowercase letter, so long as letters alternate throughout the string. '''


def myfunc(mystring):
    pos = 0
    return_string =""
    for char in mystring:
        if pos %2 ==0:
            return_string = return_string + char.upper()
        else:
            return_string = return_string + char.lower()
        pos = pos+1
    return return_string


print(myfunc("HelloWorld"))

