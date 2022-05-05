"""Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.

Example:
h = 0
m = 1
s = 1

result = 61000
Input constraints:

0 <= h <= 23
0 <= m <= 59
0 <= s <= 59"""


def past(h, m, s):
    # 1 second is 1000 miliseconds
    # 1 minute is 60000 miliseconds
    # 1 hour is 3600000 miliseconds
    hours_to_ms = h * 3600000
    min_to_ms = m * 60000
    s_to_ms = s * 1000
    result = hours_to_ms + min_to_ms + s_to_ms
    return result