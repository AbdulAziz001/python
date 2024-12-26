print("*************Iterating using for ***********************")

my_iterable = [1, 2, 3]
for item in my_iterable:
    print(item)

print("********** odd and even number display *******************")
# odd and even number display
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    if number % 2 == 0:
        print(f"{number} is even ")
    else:
        print(f"{number} is odd ")

print("********* sum of even and odd numbers  *************************")
# sum of even and odd numbers
# odd and even number display
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = 0
odd_sum = 0
for number in numbers:
    if number % 2 == 0:
        even_sum = even_sum + number
    else:
        odd_sum = odd_sum + number

print(f"even number sum is {even_sum}")
print(f"odd number sum is {odd_sum}")

print("***************  for with string ******************************")
# for with string
mystring = "hello world"
for character in mystring:
    print(character)

print("************* don't want to use variable name **************************")

# don't want to use variables
for _ in mystring:
    print("hello")

print("************* for loop with tuples **************************")
# for loop with tuples
my_tup = (1, 2, 3)
for value in my_tup:
    print(value)

print("*************** tuples unpacking in list ***********************")
# tuples unpacking in list
my_list = [(1, 2), (3, 4), (5, 6)]
for a, b in my_list:
    print(a)
    print(b)

print("****** another way of displaying *************************")
for c, d in my_list:
    print(c)

print("*************** tuples with 3 elements in list and its unpacking ************************")
# tuples with 3 elements in list and its unpacking
my_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in my_list:
    print(a)
    print(b)
    print(c)

print("************** dictionary and for loops  *************************")
# dictionary and for loops
d = {'k1': 1, 'k2': 2, 'k3': 3}
for item in d:
    print(item) # displays just keys

print("************** display key values in tuples  *************************")
for item in d.items():
    print(item) # displays keys  and values

print("************** unpacking using key value pair  *************************")
for key, value in d.items():
    print(key) # displays keys
    print(value)

print("************** unpacking using  value pair but display only values *************************")
for value in d.values():
    print(value)

