"""
ANIMAL CRACKERS: Write a function that takes a two-word string and returns True if both words begin with same letter¶

animal_crackers('Levelheaded Llama') --> True
animal_crackers('Crazy Kangaroo') --> False

"""


def animal_crackers(animal):
    split_animal = animal.split(" ")
    first_char_of_first_letter = split_animal[0][:1]
    first_char_of_second_letter = split_animal[1][:1]
    if first_char_of_first_letter == first_char_of_second_letter:
        return True
    else:
        return False


print(animal_crackers('Levelheaded Llama'))  # returns True

print(animal_crackers('Crazy Kangaroo'))  # returns False

