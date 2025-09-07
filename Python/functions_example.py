import re
import shutil
import os

# def my_add(x,y):
#     return x + y

# print("Tinh tong:", my_add(5,10))

# def copy_files(source_dir,dest_dir):
#     list_name = os.listdir(source_dir)
#     for file_name in list_name:
#         shutil.copyfile(os.path.join(source_dir, file_name),os.path.join(dest_dir, file_name))
#         # shutil.copy(os.path.join(source_dir, file_name),os.path.join(dest_dir, file_name))

# source_dir = "Source"
# dest_dir = "Destination"

# copy_files(source_dir,dest_dir)

""" Tham so truyen vao ham co the la 1 hoac nhieu 
    a: required
    b: optional - default = 0
    *c: optional - multiple
"""

# def solonnhat(a,b = 0,*c):
#     if a > b:
#         sln = a
#     else:
#         sln = b
    
#     for x in c:
#         if x > sln:
#             sln = x
    
#     return sln

# print(solonnhat(1,6,3,8,5))

""" Trong python, tham so truyen vao ham luon la tham chieu """

# def my_func(x):
#     x = 10
#     return x

# m = 5
# y = my_func(m)
# print("y: ",y)
# print("m: ",m)

# def my_func1(x):
#     x.append(3)
#     return x

# n = [1,2]
# z = my_func1(n)
# print("z: ",z)
# print("n: ",n)


""" ham lambda """
# total = lambda a,b,c: a + b + c

# print("Tong 3 so:",total(1,2,3))

# lst = [1,2,3,4,5,6,7,8]
# new_lst = set(filter(None,lst))
# print(new_lst)

""" ham de quy recursive , phai co dieu kien stop"""
def tinh_giai_thua(n):
    return tinh_giai_thua(n-1) * n if n > 1 else 1

print(tinh_giai_thua(3))
