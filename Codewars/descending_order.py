"""Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321"""
num = 42145

def descending_order(num):
    new_str = ''
    make_str = str(num)
    list_of_int_strings = [i for i in make_str]
    list_of_ints = [int(i) for i in list_of_int_strings]
    list_of_ints = sorted(list_of_ints, reverse=True)
    for i in list_of_ints:
        new_str += str(i)
    return int(new_str)

descending_order(num)


