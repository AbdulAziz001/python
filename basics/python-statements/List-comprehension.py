# way to create list easily

word = "hello world"
mylist = [letter for letter in word]
print(mylist)

"""
output 
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
"""

# Use for, split and if to  create a Statement that will print out words that start with 's'
st = 'Print only the words that start with s in this sentence'
for word in st.split():
    if word[0].startswith('s'):
        print(word)

"""
start
s
sentence
"""

# Use range() to print all the even numbers from 0 to 10.
for x in range(0, 11):
    print(x)

"""
output 
0
1
2
3
4
5
6
7
8
9
10

"""
print(" another one ")
# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
mylist = range(0, 51)
for x in mylist:
    if x % 3 == 0:
        print(x)

my_list = [x%3 == 0 for x in range(1, 51)]
print(my_list)

# Go through the string below and if the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word) % 2 == 0:
        print(f" {word} is even charactered number ")

"""
output 
 word is even character number 
 in is even character number 
 this is even character number 
 sentence is even character number 
 that is even character number 
 an is even character number 
 even is even character number 
 number is even character number 
 of is even character number 
"""

