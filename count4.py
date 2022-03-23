def counter(list):
    count = 0
    for n in list:
        if n == 4:
            count += 1
    return count

print(counter([1, 4, 6, 7, 4]))
print(counter([1, 4, 6, 7, 4, 4]))