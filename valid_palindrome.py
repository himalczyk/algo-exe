s = "A man, a plan, a canal: Panama"


def isPalindrome(self, s: str) -> bool:
    # delete all alphanumeric characters (alphabet or numbers)
    new_string = ''.join(e for e in s if e.isalnum())
    # make them all lowercase
    new_string = new_string.lower()
    # return true if characters forwards equal the characters backwards. Otherwise it is not a palindrome
    return True if new_string == new_string[::-1] else False
