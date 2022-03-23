# Volume of a sphere is 4/3 * pi * cube of radius
from math import pi

def volume_calculator(radius):
    volume = 4 / 3 * pi * radius ** 3
    return(volume)

print(volume_calculator(6))