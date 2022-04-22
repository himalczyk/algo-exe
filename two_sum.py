def twoSum(nums: list, target: int) -> list:
    first = int()
    second = int()
    for i, index in enumerate(range(0, len(nums))):
        first = nums[i]
        second = nums[i+1]
        first_index = index
        second_index = index+1
        addition = first + second
        if addition == target:
            return [first_index, second_index]
        
# 