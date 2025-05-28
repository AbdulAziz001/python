"""
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
"""


def paper_doll(text):
    final_string = ''
    for char in text:
        final_string = final_string + char * 3
    return final_string


print(paper_doll('Hello'))
print(paper_doll('Mississippi'))

