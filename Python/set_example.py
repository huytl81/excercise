# print("============================================")
# print("Set")
# print("============================================")

my_set = {"a", "b", "c", 1, 3.5, True,"abc", (1,2)}
my_set_1 = {'a', 'b', 'c', 'd'}
my_set_2 = {'c', 'd', 'e', 'f'}

# from typing import Union, Tuple
# my_set: set[Union[str, int, float, bool, Tuple[int, int]]] = {"a", "b", "c", 1, 3.5, True, (1, 2)}

# print("Type of my_set:", type(my_set))
# print("my_set:", my_set)
# my_set_empt: set[str] = set()

# for item in my_set:
#     print(item)

# my_set.add("new item")
# print("my_set after add new item:", my_set)

# my_set.update(["new item 1", "new item 2"])
# print("my_set after update:", my_set)

# my_set.remove("c")
# print("my_set after remove c:", my_set)

# my_set.discard("abc")
# print("my_set after discard abc:", my_set)

# my_set.pop()
# print("my_set after pop:", my_set)

# clear de xoa vung nho
# my_set.clear()
# print("my_set after clear:", my_set)

# del xoa bien my_set
# del my_set
# print("my_set after delete:", my_set)

# intersection_set = my_set_1.intersection(my_set_2)
# print(intersection_set)

# intersection_set = my_set_1.intersection_update(my_set_2)
# print(my_set_1)

# union_set = my_set_1.union(my_set_2)
# print(union_set)

# difference_set = my_set_1.difference(my_set_2)
# print(difference_set)

# my_set_2_updated = my_set_2.difference_update(my_set_1)
# print(my_set_2_updated)

# symmetric_diff_set = my_set_1.symmetric_difference(my_set_2)
# print(symmetric_diff_set)

# symmetric_diff_set = my_set_1.symmetric_difference_update(my_set_2)
# print(symmetric_diff_set)

# isdisjoint_set = my_set_1.isdisjoint(my_set_2)
# print(disjoint_set)

# issubset_set = my_set_1.issubset(my_set_2)
# print(issubset_set)

# issuperset_set = my_set_2.issuperset(my_set_1)
# print(issuperset_set)

# print("============================================")
# print("set comprehension")
# print("============================================")

# my_string = "hello 500 anh em"
# new_set = set(letter for letter in my_string)
# new_set1 = {letter for letter in my_string}
# print(new_set)
# print(new_set1)