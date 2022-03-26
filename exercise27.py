# Write a Python program to concatenate all elements in a list into a string and return it.

def stringer(list):
    target = ""
    for thing in list:
        target += str(thing)
    return target 
    

print(stringer([1, 5, 2, 7]))
print(stringer([1, -5.4, 123234, "asdf"]))