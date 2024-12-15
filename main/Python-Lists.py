####
# List are ordered sequence of objects
# stores multiple types of objects
# since these are indexed they can be referenced like string
####

# prints my_list
my_list = [1, 2, 3, 4, 5]
print(my_list)

# fetch the object at index 1 i.e 2
print(my_list[1])

# fetch the object starting at index 1 all the way till the end , i. 2 till 5
print(my_list[1:])

# length of list, i.e = 5
print(len(my_list))

# concatenate two list
my_another_list  = ['One', 'Two', 'Three', 'Four']
concatenated_list = my_list + my_another_list
print(concatenated_list)

# Lists are mutable, their value can be changed
concatenated_list[0] = 0
print(concatenated_list)

# append method appends a element at the end of the list
concatenated_list.append('Five')
print(concatenated_list)

# similary you can remove items from list using pop() method
# pop removes the last element from list
concatenated_list.pop()
print(concatenated_list)

# pop at a specific position like 3rd index i.e value 3 is removed
concatenated_list.pop(2)
print(concatenated_list)

# sort

unsorted_list = ['Four', 'Seven', 'Two', 'One']
# sorts this like ['Four', 'One', 'Seven', 'Two']
unsorted_list.sort()
print(unsorted_list)

# let us try sorting numbers
number_unsorted_list = [5, 3, 7, 8, 1]
# outputs the value [1, 3, 5, 7, 8]
number_unsorted_list.sort()
print(number_unsorted_list)


# reversse works the way it is
# O/p is [8, 7, 5, 3, 1]
number_unsorted_list.reverse()
print(number_unsorted_list)

