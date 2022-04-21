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

# other solution, faster

def containsDuplicate_two(nums: list) -> bool:
    hashset = set()
    
    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False