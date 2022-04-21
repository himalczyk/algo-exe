nums = [1,2,3,1]

def containsDuplicate(nums: list) -> bool:
    numbers = {}
    for i in nums:
        print(f'number: {i}')
        if i in numbers:
            return True
        numbers[i] = True
    return False

print(containsDuplicate(nums))