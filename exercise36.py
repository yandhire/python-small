# Write a Python program to add two objects if both objects are an integer type.

def add_two(o1, o2):
    if isinstance(o1, int) and isinstance(o2, int):
        return o1 + o2
    else:
        return "Both inputs have to be integers."

print(add_two(1, 2))
print(add_two(1, 2.3))
print(add_two("1", 2))
print(add_two("1", "2"))
print(add_two(5, 7))