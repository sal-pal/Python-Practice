"""
CHALLENGE DESCRIPTION

     Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling add_dots("test") should return the string "t.e.s.t".

     Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test".

     If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.

     (You may assume that the input to add_dots does not itself contain any dots.)

"""


def separate(str):
    arr = []
    for char in str:
        arr.append(char)
    return arr




def add_dots(string):
    staging_list = []
    split_string = separate(string)
    
    for char in split_string:
        dot_added = char+"."
        staging_list.append(dot_added)
        
    joined_string = "".join(staging_list)
    last_dot_removed = joined_string[:len(joined_string)-1]
    return last_dot_removed
    
 
 
 
def remove_dots(string):
    split_string = string.split(".")
    dots_removed = "".join(split_string)
    return dots_removed
 
    
    
print(add_dots("test"))
print(remove_dots(add_dots("test")))
