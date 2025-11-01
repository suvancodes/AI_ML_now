import numpy as np

## create array using numpy
## create a 1d array
# arr_1d  = np.array([1, 2, 3, 4, 5])
# print(arr_1d.ndim)              # it tell the dimsion of the array
# print(arr_1d)
# print(type(arr_1d))
# print(arr_1d.shape)  # shape of the array (no_row,no_col)


# create a 2d array

# arr2 = np.array([1, 2, 3, 4, 5])

# arr2.reshape(1,5)  # reshape the array to 1 row and 5 columns
# print(arr2)

# create a 2d array directly

# arr2 = np.array([[1, 2, 3, 4, 5]])
# print(arr2)
# print(type(arr2))
# print(arr2.shape)  # shape of the array


# arr2 = np.array([[1, 2, 3, 4, 5],[2,3,4,5,6]])
# print(arr2)
# print(arr2.shape)

# np.arange('start_ele','end_ele - 1','stap')

# print(np.arange(0,10,2).reshape(5,1))

# np.ones(('no_row','no_col')) -> it make a mayrix who's all element are one

# print(np.ones((3,3)))

# np.zeros(('no_row','no_col')) -> it make a mayrix who's all element are zeros

# print(np.zeros((3,3)))

# create identity matrix

# print(np.eye(3))




# numpy vectorrize ooperation

# arr1 = np.array([1,2,3,4,5])
# arr = np.array([1,2,3,4,5])

# # addition
# print(arr1+arr)


# universal function 

# arr = np.array([2,3,4,5,6])

# # squre root
# print(np.sqrt(arr))

# # expontial
# print(np.exp(arr))

# # sine 
# print(np.sin(arr))

# # log
# print(np.log(arr))

# indexing and sliceing

# arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(arr)

# print(arr[1:,1:])
# print(arr[0:2,1:])

# print(arr[1:,1:])


# modify the element 

# arr[0,0] = 100
# print(arr)

# by sliceing
# arr[1:] = 100
# print(arr)



# statistical concepts -- normilazition

# data = np.array([1,2,3,4,5])

# # calculate mean and standard division 
# mean = np.mean(data)
# std_div = np.std(data)
# normilazition_data = (data-mean)/std_div

# print("normilazition data: ",normilazition_data) 


# data = np.array([1,2,3,4,5,6,7,89,10])

# # mean
# mean = np.mean(data)
# print(mean)

# # median
# median = np.median(data)
# print(median)

# # standard division 
# std_div = np.std(data)
# print(std_div)

# # varience
# var = np.var(data)
# print(var)


# logical operation

# data = np.array([1,2,3,4,5,6,7,8,9])
# print(data[data>5]) ##[6,7,8,9]
# print(data[(data>=5) & (data<=8)]) ##[5,6,7,8]


