ar = [5,3,6,2]

n = len(ar)
for i in range(n):
    for j in range(n-i-1):
        if(ar[j]>ar[j+1]):
            ar[j],ar[j+1] = ar[j+1],ar[j]

print(ar)

ar.sort(reverse=1)
print(ar)



