def even_or_odd(n):
    if n % 2 == 0:
        return "number is even"
    elif n % 2 != 0:
        return "number is odd"

print(even_or_odd(5))
print(even_or_odd(4))
print(even_or_odd(0))
print(even_or_odd(7))