# Printing a group of numbers as list and tuples

numbers = input("Please input some numbers separated by commas.\n")

list = numbers.split(",")
print(list)
print(tuple(list))