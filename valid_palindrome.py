s = "A man, a plan, a canal: Panama"


def isPalindrome(self, s: str) -> bool:
    hashmap = {}
    new_string = ''.join(e for e in s if e.isalnum())
    new_string = new_string.lower()
    for index, letter in enumerate(new_string):
        hashmap[letter] = index
    reversed_string = reversed(new_string)
    for index, i in enumerate(reversed_string):
        if not hashmap[i] == index:
            return False
    return True
