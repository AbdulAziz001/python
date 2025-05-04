# 1. Dictionaries are unordered collection of key value pairs
# 2. written in curly braces
# 3. Has key and values

dict_values = {'key1':'value1', 'key2': 'value2'}
print(dict_values)

# get all the keys from dictionary dict_values, returns a list of all keys
# O/p :: dict_keys(['key1', 'key2'])
print(dict_values.keys())

# get all the values from dictionary dict_values, returns a list of all values
# O/p :: dict_values(['value1', 'value2'])
print(dict_values.values())

# get a value based on key
# O/p :: value1
print(dict_values['key1'])

# one of the use case could be prices_lookup
prices_lookup = {'apples': 15,
                 'banana': 5,
                 'oranges': 8
                 }
print(f"price of banana is {prices_lookup['banana']}")

# One interesting thing we can is
# prepare a list of prices
# sort them in ascending order or their prices
prices_lookup['grapes'] = 30
prices_lookup['dragon fruit'] = 100
prices_lookup['pears'] = 50

price_list = list(prices_lookup.values())
sorted_price_list = price_list.sort(reverse=False)
print(price_list)

# adding list to dictionary
dictionary = {'key1': 'value1',
              'list': ['a', 'b', 'c']
             }
print(dictionary)

# get the value at 2nd index position of list
# capitalize it
print(dictionary['list'][2].upper())


# Add a new key value to existing dictionary
dictionary['key3'] = 'value3'
print(dictionary)

