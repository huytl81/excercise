# print("============================================")
# print("List")
# print("============================================")

my_list = [1,2, "hello anh em", 3.5, True, [4,5,6]]
my_list2 = ["anh", "em", "minh", "la", "ban", "be"]
my_list3 = ["hgj", "abc", "xyz"]
my_list4 = [1,3,8,8,-10,9,7,8,10,8,3]

# print("My List type:", type(my_list))
# print("My List values:", my_list)
# print("Length of my_list:", len(my_list))
# print("Index 0:", my_list[0])
# print("Index 4:", my_list[4])
# print("Index -1:", my_list[-1])
# print("Index -2:", my_list[-2])
# print("Slice [1:3]:", my_list[1:3])
# print("Slice [1:]:", my_list[1:])
# print("Slice [:-1]:", my_list[:-1])
#

# for x in my_list:
#     print(x)

# my_list += my_list2

# my_list[2] = my_list[2].upper()

my_list.append(my_list3)
print("My List after append:", my_list)

my_list.extend(my_list3)
print("My List after extend:", my_list)

# my_list3.sort(reverse=True)
# print("My List 3 after sort:", my_list3)

# new_list2 = sorted(my_list2)
# print("New List 2 after sorted():", new_list2)

# print("My List 2:", my_list2)
# my_list2.reverse()
# print("My List 2 after reversed():", my_list2)

# my_list4.insert(2, 100)
# print("My List 4 after insert:", my_list4)

# my_list4.remove(6)
# print("My List 4 after remove:", my_list4)

# del my_list4[3]
# print("My List 4 after del:", my_list4)

# popped_item = my_list4.pop()
# print("My List 4 after pop:", my_list4)

# print("Index of 8 in My List 4:", my_list4.index(8,4,9))

# print("Index of 8 in My List 4:", my_list4.count(8))

# my_list5 = my_list4.copy()
# print("My List 5 after copy from 4:", my_list5)

# my_list4.clear()
# print("My List 4 after clear:", my_list4)

# print("============================================")
# print("list comprehension")
# print("============================================")

# """ list normal """
# lst = [1,2,3,4,5]
# new_lst = []
# for x in lst:
#     new_lst.append(x ** 2)
# print(new_lst)

# """ list comprehension """
# new_lst_compre = [x ** 2 for x in lst]
# print(new_lst_compre)

# # filter element
# odd_lst = [x for x in lst if x % 2 == 1]
# print(odd_lst)

# # plus 2 to odd index [3,2,5,4,7]
# plus_2_odd_index = [x if x % 2 == 0 else x + 2 for x in lst]
# print(plus_2_odd_index)

# a = int(input("Nhap so a: "))
# b = int(input("Nhap so b: "))
# new_lst = [x for x in range(a,b) if x % 2 ==0]
# print(new_lst)
