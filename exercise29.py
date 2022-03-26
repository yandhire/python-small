# Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2.

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

# My solution:
#for color in color_list_1:
#    if color in color_list_2:
#        continue
#    else:
#        print(color)

# A better solution:

print(color_list_1.difference(color_list_2))
print(color_list_2.difference(color_list_1))