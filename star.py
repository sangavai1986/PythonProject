
def pyfunc(r):
    for x in range(r+1):
        print()
        for i in range(r-x):
            print(" ",end="")
        for k in range(1,2*x):
               print("*",end="")
    for y in range(r-1):
        x = x -1
        print()
        for i in range(r -x):
            print(" ", end="")
        for k in range(1, 2 * x):
            print("*", end="")
    print()
    bool = True
    a = 0
    while(r<=3):
        if(a<0):
            break
        if(a==3):
            bool = False
        if(bool):
            a = a+ 1
        else:
            a = a - 1
        print("*"*a)
pyfunc(3)





