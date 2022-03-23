# Program to get the difference between a given number and 17
# If the number is greater than 17 return double the absolute difference.

def function(num):
    if num <= 17:
        return num - 17
    else:
        return 2 * (num - 17)

print(function(5))
print(function(19))