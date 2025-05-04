from random import shuffle


def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("Owesome you guessed it right ")
    else:
        print("Sorry ! Wrong Guess ")
        print(mylist)


def get_user_guess():
    guess = ''
    while guess not in ['0', '1', '2']:
        guess = input(" Pick a number: 0, 1 2: ")
    return int(guess)


def shuffle_my_list(my_list):
    shuffle(my_list)
    return my_list


# create a list 
my_list = ['', 'O', '']

# shuffle a list
shuffled_list = shuffle_my_list(my_list)

# get user input
input_guess = get_user_guess()

# check the index position
check_guess(shuffled_list, input_guess)