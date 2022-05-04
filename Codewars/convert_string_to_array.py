"""Write a function to split a string and convert it into an array of words.

Examples (Input -> Output):
* "Robin Singh" ==> ["Robin", "Singh"]

* "I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]"""

def string_to_array(s):
    s_array = s.split()
    return s_array if len(s_array) > 0 else ['']
    