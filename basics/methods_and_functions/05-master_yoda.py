"""
MASTER YODA: Given a sentence, return a sentence with the words reversed
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'

"""


def plain_reverse(my_string):
    return my_string[::-1]


def master_yoda(my_string):
    return ' '.join(my_string.split()[::-1])


print(master_yoda("I am home"))

