#Receiving a filename, determining the extension of said file.

file = input("Please enter a filename.\n")
extension = file.split(".")[-1]

if "." in file and extension != '':
    print("Our file's extension is: " + repr(extension))
else:
    print("Filename has no extension.")