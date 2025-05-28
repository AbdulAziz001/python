import string

def ispangram(str1, alphabet = string.ascii_lowercase):
    # Check if each letter of the alphabet appears in `t`
    for letter in alphabet:
        if str1.lower().count(letter) == 0:
            print(False)
            break
    else:
        print(True)


ispangram('The quick brown fox jumps over the lazy dog')


