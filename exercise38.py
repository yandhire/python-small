# Write a Python program to solve (x + y) * (x + y).

def calculate(x, y):
    solution = (x + y) ** 2
    print(("{} + {} ^ 2 = {}").format(x, y, solution))
    
calculate(4, 3)
calculate(7, 2)