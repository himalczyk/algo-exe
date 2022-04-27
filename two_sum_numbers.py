array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

def twoNumberSum(array, targetSum):
    # create hashmap to store checked numbers
    hashmap = {}
    # traverse through the array with index, element enumerate method
    for index, number in enumerate(array):
        # check the opposite equation to getting the targetSum
        summing = targetSum - number
        # if equation number is found in the hashmap, return the number that lead to it and the equation result itself
        if summing in hashmap:
            return [number, summing]
        # if the summing is not in the hashmap, add it to the hashmap
        # summing = 10-11 = -1, adding until number = -1, if there: summing = 10-(-1) = 11, 11 is in the hashmap, and sum = 11+(-1) = 10, true result
        hashmap[number] = True
    return []

print(twoNumberSum(array, targetSum))