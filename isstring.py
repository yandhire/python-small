def newstring(s):
    if len(s) >= 2 and s[:2] == "Is":
        return (s)
    else:
        return "Is" + s

print(newstring("Array"))
print(newstring("IsArray"))