# Write a Python program to print without newline or space.

def newprinter(printed, number):
    for i in range(0, number):
        print(printed, end="")
    print("\n")

newprinter("*", 50)
newprinter("yiğit", 10)