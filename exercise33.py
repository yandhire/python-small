# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

def sum_of_3(n1, n2, n3):
    if n1 == n2 or n2 == n3 or n1 == n3:
        return 0
    else:
        return n1 + n2 + n3
    
print(sum_of_3(1, 2, 3))
print(sum_of_3(3, 2, 3))
print(sum_of_3(2, 2, 3))
print(sum_of_3(1, 2, 2))