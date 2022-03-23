# Write a Python program to check whether a specified value is contained in a group of values.

def checker(list, n):
    for num in list:
        if n == num:
            return True
    return False

        
print(checker([1, 5, 8, 3], 3))
print(checker([1, 5, 8, 3], 8))
print(checker([1, 5, 8, 3], -1))