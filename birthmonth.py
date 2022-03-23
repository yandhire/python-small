# Little Python program to print someone's birth month's calendar.
import calendar

def birthMonth():
    year = int(input("Please enter your birth year.\n"))
    month = int(input("Please enter your birth month.\n"))
    return(calendar.month(year, month))

print(birthMonth())