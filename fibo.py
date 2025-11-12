def fibon(n):
    a = 0
    b = 1
    count = 0
    if( n < 0 ):
        print("Incorrect output")
    elif( n == 0 ):
        print(0)
    elif ( n == 1):
        print(1)
    else:
        while( count < n):
            print(a)
            c = a + b
            a = b
            b = c
            count +=1


fibon(7)
