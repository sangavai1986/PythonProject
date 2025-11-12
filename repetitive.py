arr = ["Java","Python","Java","Python","Java"]
dup = set(arr)
print(dup)
'''
seen = set()
duplicates = set()
for item in arr:
    if item in seen:
        duplicates.add(item)
    else:
        seen.add(item)
print(duplicates)
'''
