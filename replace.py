
str = "book for beginners"
str = str.replace("b","d")
print(str)
nam = "Sahhhhhhhhhhhhhhhhhhhhhhhh"


if(len(nam) < 3):
    print ("name must be atleast 3 characters")
elif (len(nam) > 50):
    print("name should be maximum 50 characters")
else:
    print("name looks good")
'''

n = 1
rows = 4
for i in range(1, rows + 1):
    # loop to print spaces
    for j in range(1, (rows - i) + 1):
        print(end=" ")

    # loop to print star
    while n != (i + 1):
        print("*",end = " ")
        n = n + 1
    n = 1

    # line break
    print()


'''