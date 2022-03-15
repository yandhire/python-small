import datetime

present = datetime.datetime.now()
printablePresent = present.strftime("%d-%m-%Y %H:%M:%S")
#Day, month, year, hour, minute, second

print("Our current date and time is {}".format(printablePresent))