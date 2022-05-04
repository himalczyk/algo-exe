"""
Given a non-empty array of integers, return the result of multiplying the values together in order. Example:

[1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24
"""

def grow(arr):
    # start with 1 to multiply the first number to what it is
    multiply = 1
    for i in arr:
        # multiply each next number with each other
        multiply *= i
    return multiply