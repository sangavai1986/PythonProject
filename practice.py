def func(x):
    for i in range(x+1):
        print()
        for j in range(x-i):
            print(" ",end = "")
        for k in range(1,2*i):
            print("*",end="")
    print()
func(3)


