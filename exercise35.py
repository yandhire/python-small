# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

def number_true(n1, n2):
    if n1 + n2 == 5 or abs(n1 - n2) == 5:
        return True
    elif n1 == n2:
        return True
    else:
        return False
    
print(number_true(3, 2))
print(number_true(7, 2))
print(number_true(7, 7))
print(number_true(9, 2))