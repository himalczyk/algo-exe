"""Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a new array of the same lenght with the squares of
the original integers also in sorted ascending order

"""

array = [1, 2, 3, 5, 6, 8, 9]

def sortedSquaredArray(array):
    placeholder = []
    for i in array:
        squaring = i ** 2
        placeholder.append(squaring)
    placeholder.sort()
    return placeholder

# less code solution

def sortedSquaredArray(array):
    squared = [i ** 2 for i in array]
    squared.sort()
    return squared