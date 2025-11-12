d = {"Name" : "Sangu", "Age" : 32}

for i in dict(d):
    print(i , d[i])


d["Shirt"] = "blue"

print(d.keys())
print(d.values())
temp = d.pop("Shirt")
print(temp)
print(d)
d.popitem()
print(d)
t1 = ("Apple", "Banana", "Apple")
t2 = ("Papaya","he", "Apple")
t3 = t1 + t2
t4 = t1 * 2
print(t4.count("Apple"))
print(t3)
print(t4)
#t[4] = "Hello"

s1 = {1,2,3}
s2 = {3,4,5}
s3 = s1 & s2
s4 = s1 - s2
s5 = s1 ^ s2
print(s3)
print(s4)
print(s5)

def pali(pattern):
    return (pattern == pattern[::-1])

print(pali("nannan"))

def anagram(pat,text):
    return(sorted(pat) == sorted(text))

print(anagram("listen","silent"))

print("LIST OPERATIONS")
l1 = [1,2,3]
l2 = [5,6]
print(l1)
l1.append(4)
print(l1)
l1.extend(l2)
print(l1)
l1.insert(2,8)
print(l1)
l1.reverse()
print(l1)
l1.sort()
print(l1)
l1.pop()
print(l1)
l1.pop(4)
print(l1)
l1.remove(1)
print(l1)

def comp(s):
    if not s:
        return ""
    result = ""
    count = 1
    for i in range(1,len(s)):
        if(s[i] == s[i-1]):
            count += 1
        else:
            result += s[i-1] + str(count)
            count = 1
    result += s[-1] + str(count)
    return result

print(comp("aaabbcccdd"))

def bubblesort(a):
    n = len(a)
    print(n)
    for i in range(n-1):
        for j in range(n-i-1):
            if(a[j]> a[j+1]):
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
    print(a)
    a.sort(reverse=1)
    print(a)

def binarysearch(ar, target):
    print(ar)
    print(target)
    l = 0;
    r = len(ar) - 1
    mid = 0
    while l <= r:
        mid = (r+l)//2
        #print(mid)
        if(ar[mid] == target):
            return mid
        if(ar[mid]< target):
            l =  mid+ 1
        if(ar[mid]>target):
            r = mid -1
    return -1

def bitwise(ar2):

    result = ar2[0] | ar2 [1]
    result = bin(result)
    result = result[2:]
    print(result)

ar = [4,3,2,10,5]
x = 3
bubblesort(ar)
ar2 = sorted(ar)

def longest(sen):
    #ar6[]
    ar6 = sen.split("[^a-z^A-Z]")
    print(ar6)

'''

result = (binarysearch(ar2,x))
print(result)
print(max(ar))
'''
ar2 = [0b1001,0b0010]
bitwise(ar2)
ar3 = [3,4,2,3,1,4]
ar4 = set(ar3)
print(ar4)

sen = "fun!& time"
longest(sen)