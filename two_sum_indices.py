nums = [2,7,11,15]
target = 9
nums_two = [3,2,4]
target_two = 6
nums_three = [3,3]
target_three = 6


def twoSum(nums: list, target: int) -> list:
    # create hashmap to store list of numbers value and index
    # hashmap = {value : index}
    hashmap = {}
    # use enumerate to have indexes and value of the current element
    for idx, i in enumerate(nums):
        # have the difference of the target and current element (number)
        diff = target - i
        # check if the diff is in the hashmap to give the opposite equation leading to the target
        if not diff in hashmap:
            # add a value : index pair to store the number
            hashmap[i] = idx
        else:
            # return the first element + the second element index giving the wanted result
            return [hashmap[diff], idx]
        
            
print(twoSum(nums, target))
print(twoSum(nums_two, target_two))
print(twoSum(nums_three, target_three))

