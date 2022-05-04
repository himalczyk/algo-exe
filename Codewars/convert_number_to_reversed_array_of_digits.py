"""
Convert number to reversed array of digits
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

Example:
348597 => [7,9,5,8,4,3]
0 => [0]
"""

def digitize(n):
    # convert string of numbers into a list using generator expression for arrays
    arr = [int(x) for x in str(n)]
    return arr[::-1]