nums = [2,7,11,15]
target = 9
nums_two = [3,2,4]
target_two = 6
nums_three = [3,3]
target_three = 6


def twoSum(nums: list, target: int) -> list:
    hashmap = {}
    for idx, i in enumerate(nums):
        diff = target - i
        if not diff in hashmap:
            hashmap[i] = idx
        else:
            return [hashmap[diff], idx]
            
print(twoSum(nums, target))
print(twoSum(nums_two, target_two))
print(twoSum(nums_three, target_three))

