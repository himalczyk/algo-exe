# Algo notes

# Contains duplicate

Loop through all the elements in the array checking if the number is there, continue with adding if not in the list.

If in the list, return True, if not just finish loop function return False.

```
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
```

# Valid anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Anagram - each string has the same number of characters.

**Use .sort() method**

Use sort method on the array to check if they are equal, if not, they never cannot be an anagram:

```
def isAnagram(s: str, t: str) -> bool:
    hashset = [letter for letter in s]
    hashset_two = [letter for letter in t]
    hashset.sort()
    hashset_two.sort()
    print(hashset)
    print(hashset_two)
    if hashset == hashset_two:
        return True
    else:
        return False

    
print(isAnagram("anagram", "nagaram"))
print(isAnagram("rat", "car"))
print(isAnagram("aa", "a"))
print(isAnagram("ab", "a"))
```

# Two sum


