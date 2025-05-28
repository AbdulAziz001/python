"""
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment)
exceeds 21, return 'BUST'
"""


def blackjack(a, b, c):
    sum_of_num = a + b + c
    if sum_of_num <= 21:
        return sum_of_num
    elif sum_of_num > 21:
        if a | b | c == 11:
            reduced_sum = sum_of_num - 10
            if reduced_sum > 21:
                return 'BUST'
            else:
                return reduced_sum
        else:
            return 'BUST'


print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))
