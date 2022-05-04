"""
Very simple, given an integer or a floating-point number, find its opposite.

Examples:

1: -1
14: -14
-34: 34
"""

def opposite(number):
    if number > 0:
        # just make the positive a negative
        number = -number
    elif number < 0:
        # two negatives equal a positive
        number = -number
    return number