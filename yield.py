def maxmin():
    ar = [45,23,67,12,90]
    yield max(ar)
    yield min(ar)
    ar.sort()
    yield ar
    ar.sort(reverse=1)
    yield ar

obj = maxmin()
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))