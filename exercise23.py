# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.

def nonnegative(string, n):
    length = 2
    if length > len(string):
        length = len(string)
    substring = string[:length]

    return substring * n

print(nonnegative("yiğit", 3))
print(nonnegative("y", 5))