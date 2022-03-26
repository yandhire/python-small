# Write a Python program to get OS name, platform and release information.

import platform
import os

print("Name of the platform: \n", os.name)
print("Name of the operating system: \n", platform.system())
print("Version of the operating system: \n", platform.release())