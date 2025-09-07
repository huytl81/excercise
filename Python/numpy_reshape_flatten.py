import numpy as np

arr = np.array([
    [[4, 5, 0], [1, 2, 3]],
    [[5, 7, 0], [3, 5, 6]],
    [[8, 9, 0], [7, 8, 9]]
])

print("array:", arr)
print("shape of array:", arr.shape)

print("reshape array:", arr.reshape(9, 2))
print("reshape array:", np.reshape(arr, (3,2,3)))

print("flatten array:", arr.flatten())
