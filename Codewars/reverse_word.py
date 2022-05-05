"""Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"""

text = 'The quick brown fox jumps over the lazy dog.'
# text = 'apple'
# text = 'a b c d'
# text = 'double  spaced  words'

def reverse_words(text):
    list_words = text.split()
    new_words = [word[::-1] for word in list_words]
    new_string = " ".join(new_words)
    return new_string

# print(reverse_words(text))

# recursion

"""Recursion is when a function calls itself in its own body. To prevent infinite recursion, 
you should provide a base case that produces a result without calling the function again. 
The second component is the recursive case, which starts the recursive loop and performs most of the computation."""