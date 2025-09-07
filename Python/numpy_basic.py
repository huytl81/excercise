""" AI Coding """

import numpy as np

# NOTE: tao array 1 chieu
my_array = np.array([1,2,3,4,5.5])

print("Phan tu dau tien:", my_array[0], my_array[-5])
print("Phan tu cuoi cung:",my_array[4], my_array[-1])

# slicing khong tao ra array moi ma la view, thay doi array goc se thay doi array moi va nguoc lai
new_array = my_array[2:]
new_array[2] = 83.38

# NOTE: tao array 2 chieu
arr_2d = np.array([[1,2,3], [4,5,6],[7,8,9]])
print("array_2d[0][0]:", arr_2d[0][0])
print("array_2d[0,0]:", arr_2d[0,0])

print("array_2d[2][2]:", arr_2d[2][2])
print("array_2d[2,2]:", arr_2d[2,2])

print("cot dau tien:", arr_2d[:,0])
print("cot dau tien:", arr_2d[0:3,0])

print("hang dau tien:", arr_2d[0,:])
print("hang dau tien:", arr_2d[0,0:3])

print("So chieu my_array:", my_array.ndim)
print("So chieu arr_2d:", arr_2d.ndim)

print("Shape of my_array:", my_array.shape)
print("Shape of arr_2d:", arr_2d.shape)

print("Type of my_array:", my_array.dtype)
print("Type of arr_2d:", arr_2d.dtype)

print("Size of my_array:", my_array.size)
print("Size of arr_2d:", arr_2d.size)

print("Array 1 chieu:", my_array)
print("Array 2 chieu:", arr_2d)

print("Type of my_array:", type(my_array))
print("Type of arr_2d:", type(arr_2d))

print("dtype of my_array:", my_array.dtype)
print("dtype of arr_2d:", arr_2d.dtype)

new_array_2d = arr_2d.astype(np.float64)
print("dtype of new_array_2d:", new_array_2d.dtype)

# NOTE: Mang theo mau zeros
zeros_arrar = np.zeros((3,4), dtype=np.int64)
print("zeros_array:", zeros_arrar)
print("dtype of zeros_array:", zeros_arrar.dtype)

# NOTE: Mang theo mau ones
ones_array = np.ones((8,), dtype=np.int16)
print("ones_array:", ones_array)
print("dtype of ones_array:", ones_array.dtype)

# NOTE: Mang theo mau empty
empty_array = np.empty((2,3))
print("empty_array:", empty_array)

# NOTE: Mang theo mau arange
arange_array = np.arange(10,20,2)
print("arange_array:", arange_array)

linspace_arr = np.linspace(0,10, num=5)
print("linspace_arr:", linspace_arr)