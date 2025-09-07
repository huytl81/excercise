"""
3 cach import module
1. import ten_module as alias
2. from ten_module import ten_func # import 1 function cu the
3. from ten_module import* # import tat ca cac function tru cac ham co dang _tenham (phai import theo cach 2)
"""
import os, sys

#current_path = os.getcwd()
#current_path = os.path.abspath(".")

#module1_path = os.path.abspath(os.path.join("my_module"))
module1_path = os.path.abspath("my_module")

sp = sys.path
sp.append(module1_path)

# for p in sp:
#     print(p)

from my_module import module1_example as module1

# NOTE: __file__ : la ten file cua module hien tai
# NOTE: __name__ : la chuoi "__main__" cua module hien tai

print(f"__file__ is:'{__file__}', __name__ is '{__name__}'")

def my_func(c,d):
    print("c - d = ", c - d)

if __name__ == "__main__":
    my_func(10,4)
    module1.func(3,8)
