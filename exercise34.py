# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

def sum_of_2(n1, n2):
    if 15 < n1 + n2 and n1 + n2 < 20:
        return 0
    else:
        return n1 + n2

print(sum_of_2(12, 4))
print(sum_of_2(12, 10))
print(sum_of_2(12, 15))
print(sum_of_2(12, 7))