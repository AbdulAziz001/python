def up_low(my_string):
    num_upper_case = 0
    num_lower_case = 0

    for char in my_string:
        if char.isalpha():
            if char.isupper():
                num_upper_case += 1
            else:
                num_lower_case += 1

    print(f"No of Upper case characters: {num_upper_case}")
    print(f"No of lower case characters: {num_lower_case}")


up_low('Hello Mr. Rogers, how are you this fine Tuesday?')


