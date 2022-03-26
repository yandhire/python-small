# Write a python program to call an external command in Python.

import os

print(os.system("dir"))

#If I were on Linux or MacOS I would instead be using:
#print(os.system("ls -l"))