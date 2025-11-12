import numpy as np
arr = np.array([10,20,30,40,50,60,70])

# printing alternate items from 2nd item to 4th item
print(arr[1:4:2])

# printing items from 2nd to 4th
print(arr[1:4])

# printing only alternate items
print(arr[::2])

# creating arr with 2 dimenstion
arr1 = np.array([10,20,30,40],dtype='S')
print(arr1)

# reshaping array from 1d to 4d
arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
arr3 = arr2.reshape(4,3)
print(arr3)

#join 2 arrays

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

#array
arr = np.array([1, 2, 3, 4, 5, 4, 4])

x = np.where(arr == 4)
print(x)