print("============================================")
print("Tuple")
print("============================================")

tuple_1 = ("apple", "banana", "cherry", "apple", 1, 3.8,"apple", True)
tuple_2 = ("apple", "banana", "cherry", "apple", 1, 3.8, True)
tuple_3 = ("apple", "banana", "cherry", "apple", 1, 3.8, True)
tuple_4 = (1,2,3,4,5,6,7,8)
tuple_5 = ("A","B","C","D","E","F","G","H")

# print(max(tuple_4))
# print(min(tuple_5))


# print(type(tuple_1))
# print("Tuple values:", tuple_1)
# print("Length of tuple_1:", len(tuple_1))
# print("Index 0:", tuple_1[0])
# print("Index 4:", tuple_1[4])
# print("Index -1:", tuple_1[-1])
# print("Slice [1:3]:", tuple_1[1:3])
# print("Slice [1:]:", tuple_1[1:])
# print("Slice [:-1]:", tuple_1[:-1])
# print("Slice/Reverse [::-1]:", tuple_1[::-1])

# for y in tuple_1:
#     print(y)

# new_tuple = ("a25", "b36", "c47")
# tuple_1 += new_tuple
# print(f"Tuple after concat:{tuple_1}")

# list_1= list(tuple_1)
# list_1.append(["new item1", "new item2"])
# tuple_1 = tuple(list_1)
# print(f"Tuple after append new item:{tuple_1}")

# print(f"Count apple: {tuple_1.count('apple')}")
print("Index of apple:", tuple_1.index("apple",2,7))
# print("ID of tuple_1:", id(tuple_1))
# print("ID of tuple_2:", id(tuple_2))
# print("ID of tuple_3:", id(tuple_3))

# # Khai bao tuple co thanh phan la list
# tuple_100 = ([1,2,3], "abc", 3.5)
# # Thay doi gia tri cua phan tu thu 2 cua list trong tuple
# tuple_100[0][2] = 39000
# print(tuple_100)