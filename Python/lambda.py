# my_func = lambda x, y: x + y
# print(my_func(4,5))

# sort list
# lst = ["Huy", "Hung", "Duc", "Minh", "Quang"]
# print(sorted(lst, key=lambda x: len(x), reverse=True))
# lst.sort(key=lambda x: len(x))
# print(lst)

# filter(func, iterable)
# lst = [1,2,3,4,5,6]
# new_lst = set(filter(lambda x: x % 2 == 0, lst))
# print(new_lst)

# map(func, iterable)
# lst = [1,2,3,4,5,6]
# new_lst  = tuple(map(lambda x: x + 3, lst))
# print(new_lst)

# reduce(func, iterable)
from functools import reduce
lst  = [1,2,3,4,5,6,7,8]
new_lst = reduce(lambda x,y: x + y, lst)
print(new_lst)

