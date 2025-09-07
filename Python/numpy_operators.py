import numpy as np

# NOTE: Toan tu cong
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr_total = arr1 + arr2
print(arr_total)

arr_minus = arr1 - arr2
print(arr_minus)

arr_mul = arr1 * arr2
print(arr_mul)

arr_div = arr2 / arr1
print(arr_div)

arr_mod = arr2 % arr1
print(arr_mod)

arr_floor = arr2 // arr1
print(arr_floor)


arr_2d = np.array([[1,2,3], [4,5,6]])
tong = arr_2d.sum()
tong_theo_cot = arr_2d.sum(axis=0, keepdims=True)
tong_theo_hang = arr_2d.sum(axis=1, keepdims=True)

print("Tong:", tong)
print("Tong theo cot:", tong_theo_cot)
print("Tong theo hang:", tong_theo_hang)


# NOTE min, max, mean

print("Min:", arr1.min())
print("Max:", arr1.max())
print("Mean:", arr1.mean())