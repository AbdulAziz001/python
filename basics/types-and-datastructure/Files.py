# IO with Basic Files in Python


myfile = open('../../resources/test.txt')
contents = myfile.read()
print(contents)

# read the file line by line
myfile.seek(0)
contents_line = myfile.readlines()
print(contents_line)

myfile.close()

# with below function you don't need to close the file
# after read , python already does that
with open('../../resources/test.txt') as my_new_file:
    contents = my_new_file.read()
    print(contents)

# let's play around with mode
with open('../../resources/test.txt', mode='r') as my_new_file:
    contents = my_new_file.read()
    print(contents)

# open file in append mode
with open('../../resources/test.txt', mode='a') as my_new_file:
    my_new_file.write("\nthis is the fourth line")

with open('../../resources/test.txt', mode='r') as my_new_file:
    contents = my_new_file.read()
    print(contents)

# mode = 'w'
with open('../resources/test_write.txt', mode='r') as my_new_file:
    my_new_file.write("I wrote this line ")
