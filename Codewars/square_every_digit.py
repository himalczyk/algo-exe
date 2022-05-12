"""Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer"""



def square_digits(num):
    list_single_ints = [number for number in str(num)]
    print(f'list_single_ints {list_single_ints}')
    make_ints = [int(number) for number in list_single_ints]
    print(f'make_ints {make_ints}')
    pow_ints = [i * i for i in make_ints]
    print(f'pow_ints {pow_ints}')
    concat = ''
    for i in pow_ints:
        concat += str(i)
    return int(concat)

square_digits(9119)