print("############ Range function ############ ")

for num in range(1, 10):
    print(num)

print("############ Range function with step ############ ")
print("############ display range in multiples of 2  ############ ")
for num in range(1, 10, 2):
    print(num)

print("############ Enumerate demo ############ ")
word = "abdcdef"
for character in enumerate(word):
    print(character)

print("############ Enumerate demo with tuples unpacking############ ")
word = "abdcdef"
for index, character in enumerate(word):
    print(index)
    print(character)

print("############ zip function ############ ")
my_list_1 = [1, 2, 3]
my_list_2 = [100, 200, 300, 400]
for item in zip(my_list_1, my_list_2):
    print(item)

print("############ in operator  ############ ")
result_false = 'x' in ['y', 'z', 'e']
print(result_false)
result_true = 'x' in ['y', 'z', 'x']
print(result_true)

result_dict_true = 'mykey' in {'mykey': 'test', 'my_key2': 'test2'}
print(result_dict_true)

print("############ min max  ############ ")
mylist = [10, 20, 30]
print(min(mylist))
print(max(mylist))

print("############ random library  ############ ")
from random import shuffle
mylist = [10, 20, 30, 40, 50, 60]
shuffle(mylist)
print(mylist)

print("############ random integer  ############ ")
from random import randint
random_number = randint(1, 100)
print(random_number)

print("############  accept user input   ############ ")
age = int(input('Enter your age'))
if age > 18:
    print(" you are eligible for vote ")
else:
    print(" you are not eligible for vote ")

"""
output 
############ Range function ############ 
1
2
3
4
5
6
7
8
9
############ Range function with step ############ 
############ display range in multiples of 2  ############ 
1
3
5
7
9
############ Enumerate demo ############ 
(0, 'a')
(1, 'b')
(2, 'd')
(3, 'c')
(4, 'd')
(5, 'e')
(6, 'f')
############ Enumerate demo with tuples unpacking############ 
0
a
1
b
2
d
3
c
4
d
5
e
6
f
############ zip function ############ 
(1, 100)
(2, 200)
(3, 300)
############ in operator  ############ 
False
True
True
############ min max  ############ 
10
30
############ random library  ############ 
[40, 50, 60, 10, 30, 20]
############ random integer  ############ 
99
############  accept user input   ############ 
Enter your age17
 you are not eligible for vote 

"""