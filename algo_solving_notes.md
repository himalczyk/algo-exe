# Algo notes

## Contains duplicate

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

## Valid anagram

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

## Two sum indices return

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

nums = [2,7,11,15]
target = 9

Create a hashmap to map the value from the list and its index using a loop with enumerate, traversing through the index, element from the list.

Use hashmap = {value : index}

Add value and index to hashmap:

hashmap = {2 : 0} etc.
value:2
index: 0

Look for the difference between target - current number
9-2 = 7
Check if 7 is in the hashmap, if not, add the current number to the hashmap
**current** hashmap = {2:0}
Keep looping
9-7 = 2
check if 2 is in the hashmap, it is, since the opposite: 7+2 gives the target, return the current number (7) and the hashmap number given from the difference

Once found the difference number in the hashmap from the equation above (target - current number)

```
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
```

## Two number sum return

Write a function that takes in a non-empty array of distinct integers and an
integer representing a target sum. If any two numbers in the input array sum
up to the target sum, the function should return them in an array, in any
order. If no two numbers sum up to the target sum, the function should return
an empty array.

```
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
```
# Pointers

## Validate Subsequence

O(n) Time ; O(1) Space

In mathematics, a subsequence of a given sequence is a sequence that can be derived from the given sequence by deleting some or no elements without changing the order of the remaining elements

Subsequence cares about order

Declare two pointers following the indexes, the position of the numbers we are currently on.

traverse through both of the sequences basing on their lenght
If match, so if number in array is equal to sequence number, increment the sequence index.
If not, just go to the next index in the initial array.
Loop finished when the arrIdx is out of range and returns True if the seqIdx is equal to the len of the sequence, which is the only possibility as all the numbers are found.

```
def isValidSubsequence(array, sequence):
	arrIdx = 0
	seqIdx = 0
	while arrIdx < len(array) and seqIdx < len(sequence):
		if array[arrIdx] == sequence[seqIdx]:
			seqIdx += 1
		arrIdx += 1
	return seqIdx == len(sequence)
```

## Valid palindrome

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

```
s = "A man, a plan, a canal: Panama"


def isPalindrome(self, s: str) -> bool:
    # delete all alphanumeric characters (alphabet or numbers)
    new_string = ''.join(e for e in s if e.isalnum())
    # make them all lowercase
    new_string = new_string.lower()
    # return true if characters forwards equal the characters backwards. Otherwise it is not a palindrome
    return True if new_string == new_string[::-1] else False

```

## Sorted Squared array

Write a function that takes in a non-empty array of integers that are sorted in ascending order and returns a new array of the same lenght with the squares of
the original integers also in sorted ascending order

array = [1, 2, 3, 5, 6, 8, 9]

```
def sortedSquaredArray(array):
    placeholder = []
    for i in array:
        squaring = i ** 2
        placeholder.append(squaring)
    placeholder.sort()
    return placeholder
```

**less code solution**

```
def sortedSquaredArray(array):
    squared = [i ** 2 for i in array]
    squared.sort()
    return squared
```


## Tournament Winner

competitions[i]
results[i] - this specifies the winner
1 in results means that the home team won
0 means that the away team won

Create a hashmap to add all the teams that were given in the current competitions array by looping over each one, checking if its in the dict and if not, add it and its score to keep track

Loop over the results, which are always as long as the competitions
Get the first elements and get the winner of that one

```
competitions = [
    ['HTML', "C#"],
    ['C#', "Python"],
    ['Python', 'HTML']
]
results = [0, 0, 1]
```


```
def tournamentWinner(competitions, results):
    # create hashmap to store teams
    teams = {}
    # loop over each matchup in competitions which is a nested linked array of arrays
    for match in competitions:
        for team in match:
            if team not in teams:
                teams[team] = 0

    # results len equals competitions number as there is always a match and a score
    while len(results) > 0:
        # get current competition
        current_match = competitions[0]
        # get current not winner, since they are with swapped places
        current_not_winner = results[0]
        # delete the not winning one
        current_match.pop(current_not_winner)
        # add points to the left team which is the winner
        teams[current_match[0]] += 3
        # delete elements from the main list to get the next winners
        competitions.pop(0)
        results.pop(0)
    # use max method to get the teams with the max value from the dict
    max_points = max(teams, key=teams.get)
    return max_points
```