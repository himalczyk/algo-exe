"""In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.

Examples
high_and_low("1 2 3 4 5")  # return "5 1"
high_and_low("1 2 -3 4 5") # return "5 -3"
high_and_low("1 9 3 4 -5") # return "9 -5"
Notes
All numbers are valid Int32, no need to validate them.
There will always be at least one number in the input string.
Output string must be two numbers separated by a single space, and highest number is first."""


def high_and_low(numbers):
    # split to create a list of each number as an element type string
    check_nums = numbers.split()
    # make each element an int
    int_nums = [int(n) for n in check_nums]
    # check for highest using the built in max() func
    highest = max(int_nums)
    # check for lowest using the built in min() func
    lowest = min(int_nums)
    return f'{str(highest)} {str(lowest)}'