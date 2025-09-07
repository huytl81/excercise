print("============================================")
print("Dictionary")
print("============================================")

# my_dict = {(1,2,['a','b']): 'abc', "key1": "value1", "key2": "value2"}
# print(my_dict)

# my_dict = {(1,2,'a','b'): 'abc', "key1": "value1", "key2": "value2"}
# print(my_dict)

# # name_age_empty1 = dict() # empty dict() or {}
# name_age_empty1: dict[str, int] = dict()
# name_age_ampty2 = {}
name_age = {"Son": 20, "Huy": 22, "Nam": 19}

# print("Type of name_age:", type(name_age))
# print("Length of name_age:", len(name_age))

# print("Keys:", name_age.keys())
# print("Values:", name_age.values())
# print("Items:", name_age.items())

# print("Age of Huy:", name_age["Huy"])
# print("Age of Nam:", name_age.get("Sen", "Not found"))

# name_age["Son"] = 33
# name_age.update({"Minh": 25})
# name_age.update(dict([("Quang", 37)]))

# del name_age
# del name_age["Nam"]

# name_age.pop("Son")
# name_age.popitem()

# name_age.clear()

# name_age_copied = name_age.copy()

# print("Dictionary:", name_age_copied)
# print("ID of name_age:", id(name_age))
# print("ID of name_age_copied:", id(name_age_copied))

#print(max(name_age))
#print(min(name_age))
#print(len(name_age))

# name_age.setdefault("Quang", 47)
# print(name_age)

# for k in name_age:
#     print(k)

# for k in name_age.keys():
#     print(k)

# for v in name_age.values():
#     print(v)

# for item in name_age.items():
#     print(item)

# for k,v in name_age.items():
#     print(f"Key: {k}, Value: {v}")

keys = ("Giam doc", "Truong phong", "Nhan vien", "Bao ve")
values = ["Nguyen Van A", "Nguyen Van B", "Nguyen Van C", "Nguyen Van D"] # values thay doi thi my_dict tu dong thay doi

# khoi tao dict cung 1 gia tri value
my_dict = dict.fromkeys(keys,"chua bo nhiem")
print(my_dict)

# khoi tao dict tu 2 tuple, set, list,...
# my_dict = dict(zip(keys, values))
# print(my_dict)

# print("============================================")
# print("dictionary comprehension")
# print("============================================")

# dic = {item: item** 2 for item in lst}
# print(dic)

# print("============================================")
# print("multiple loops")
# print("============================================")

# nested_list = [[i for i in range(3)] for _ in range(8)]
# print(nested_list)

# arr_3d = [
#     [[4, 5], [1, 2, 3]],
#     [[5, 7], [3, 5, 6]],
#     [[8, 9], [7, 8, 9]]
# ]
# flattened_lst = [num for d0 in arr_3d for d1 in d0 for num in d1]
# print(flattened_lst)