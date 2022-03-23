# Write a Python program to test whether a number is within 100 of 1000 or 2000.

from tabnanny import check


def checking(num):
    if abs(1000 - num) <= 100:
        print("Number is around 100 of 1000")
    elif abs(2000 - num) <= 100:
        print("Number is around 100 of 2000")
    else:
        print("Number is not around that range.")

checking(1000)
checking(9000)
checking(900)
checking(800)
checking(2090)