# Set is unordered collection of unique objects


# create a set

myset = set()
myset.add(1)

print(myset)

myset.add(2)
print(myset)

# convert list to set to remove duplicates

my_list = [1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4]
new_set = set(my_list)
print(new_set)
