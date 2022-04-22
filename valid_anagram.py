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
