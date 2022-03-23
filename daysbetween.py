# Little program to count the days between 2 different dates.
# I built this to show the time difference between my birth date and current date

from datetime import date

birthdate = date(2001, 12, 5)
today = date.today()
difference = today - birthdate
print(difference)