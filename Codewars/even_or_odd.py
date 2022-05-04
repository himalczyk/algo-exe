"""
Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
"""

def even_or_odd(number):
    # Here num % 2 will equal 0 if num is even and 1 if num is odd. Checking against 0 will return a Boolean of True or False based on whether or not num is even.
    return "Even" if number % 2 == 0 else "Odd"
