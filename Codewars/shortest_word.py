"""Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types."""

def find_short(s):
    list_of_words = s.split()
    list_of_lenghts = [len(word) for word in list_of_words]
    l = min(list_of_lenghts)
    return l # l: shortest word length