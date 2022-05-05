array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]

# O(n) Time ; O(1) Space

# In mathematics, a subsequence of a given sequence is a sequence that can be derived from the given sequence by deleting some 
# or no elements without changing the order of the remaining elements

# Subsequence cares about order

# Declare two pointers following the indexes, the position of the numbers we are currently on.

# traverse through both of the sequences basing on their lenght
# If match, so if number in array is equal to sequence number, increment the sequence index.
# If not, just go to the next index in the initial array.
# Loop finished when the arrIdx is out of range and returns True if the seqIdx is equal to the len of the sequence, which is the only possibility as all the numbers are found.


def isValidSubsequence(array, sequence):
	arrIdx = 0
	seqIdx = 0
	while arrIdx < len(array) and seqIdx < len(sequence):
		if array[arrIdx] == sequence[seqIdx]:
			seqIdx += 1
		arrIdx += 1
	return seqIdx == len(sequence)