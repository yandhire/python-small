# Calculate the sum of three given numbers, if the values are equal then return thrice of their sum

def sumof3(a, b, c):
    if a == b == c:
        sum = a * 9
        # If all 3 numbers are the same their sums would be one of them times three
        # But we want to return the sum times three, so we multiply it by nine
    else:
        sum = a + b + c
    
    return(sum)

print(sumof3(3, 3, 3))
print(sumof3(1, 2, 3))