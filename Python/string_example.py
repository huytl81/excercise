# print("============================================")
# print("String")
# print("============================================")

# my_str = "Hello Huy"
# print("my_str:", my_str)
# print("Type of my_str:", type(my_str))
# print("Length of my_str:", len(my_str))
# print("Index 0:", my_str[0])
# print("Index 4:", my_str[4])
# print("Index -1:", my_str[-1])
# print("Index -2:", my_str[-2])
# print("Slice [1:3]:", my_str[1:3])
# print("Slice [1:]:", my_str[1:])
# print("Slice [:-1]:", my_str[:-1])

# for ch in my_str:
#     print(ch.upper())

# if "Hello" in my_str:
#     print("Hello" in my_str)

# print("============================================")
# print("Boolean")
# print("============================================")

# num = 15;
# print("20 = 10:",20 == 10)
# print("20 >= 10:", 20 >= 10)
# print("Number is in range [10,20]:", num >= 10 and num <= 20)

# format string

name = "Huy Ta"
weight = 9.65
accuracy = 0.3489562345

""" modulo operator % """
# my_str = "My name is %s, I weight %s kg" % (name, weight)
# my_str = "My name is %s, I weight %.3f kg" % (name, weight)


""" .format()"""
# my_str = "My name is {}, I weight {} kg".format(name, weight)
# my_str = "My name is {1}, I weight {0} kg".format(weight, name)
# my_str = "My name is {x}, I weight {y} kg".format(x=weight, y=name)

# dict = {"name": "Huy Ta", "weight": 6.9}
# my_str = "My name is {name}, I weight {weight} kg".format(**dict)
# my_str = "My name is {my_dict[name]}, I weight {my_dict[weight]} kg".format(my_dict=dict)
# my_str = "accuracy: {:.6f}".format(accuracy)

""" f-string """
#my_str = f"My name is {name}, I weight {weight} kg"
# my_str = f"accuracy: {accuracy:.6f}"

""" template """
# from string import Template
# my_temp = Template("My name is $ho_ten, I weight $can_nang kg")
# my_str = my_temp.substitute(ho_ten=name, can_nang=weight)

# print(my_str)

""" str[m:n] """
# my_str = "Nhu co bac Ho trong ngay vui dai thang"
# print(my_str[3:13])
# print(my_str[:13])
# print(my_str[3:])

""" chr() """
#c = 65 # ascii
# print(chr(c))

""" repr() """
# print(repr(c))

""" str() """
# print(str(c))

"""choice"""
# from random import choice
# print(choice("abcdefg")) # random charactor in string

""" s.center(), s.ljust(), s.rjust(), s.lower(), s.upper(), s.strip(), s.lstrip(), s.rstrip(), s.zfill(), s.swapcase(). s.title() """
# s = """Hom nay troi \t Mua to qua
# em khong di \t ra ngoai duoc
# nen khong mua banh my an
# """
# print(s.center(20,"*"))
# print(s.ljust(20,"-"))
# print(s.rjust(20,"="))
# print(s.lower())
# print(s.upper())
# print(s.strip())
# print(s.lstrip())
# print(s.rstrip())
# print(s.zfill(20))
# print(s.swapcase())
# print(s.title())

""" s.count(), s.find(), s.index(), s.startswith(), s.join(), len(s), s.replace() """
# print(s.count("my", 0, 15))
# print(s.find("my"))
# print(s.index("my"))
# print(s.startswith("H"))
# print(s.endswith(" "))
# print(s.join(["@@@","###","$$$"]))
# print(len(s))
# print(s.replace(" ","+"))

""" s.split(), s.splitlines(), s.expandtab() """
# print(s.split(" ",3))
# print(s.splitlines(True))
# print(s.expandtabs(40))

""" s.encode(), s.decode() """
# print(s.encode("utf-16"))
# print(s.encode("utf-16").decode("utf-16"))

""" min(s), max(s) """
# ma ascii lon nhat hoac nho nhat
# print(min(s))
# print(max(s))

""" s.isdecimal(), s.isalpha(), s.islower(), s.isupper(), s.isdigit(), s.isnumeric(), s.isalnum(), s.isspace(), s.istitle() """
# s = "ab1234cd"
# print(s.isdecimal())
# print(s.isalpha())
# print(s.islower())
# print(s.isupper())
# print(s.isdigit())
# print(s.isnumeric())
# print(s.isalnum())
# print(s.isspace())
# print(s.istitle())

""" %s, %i, %d, %u, %f, %x, %e """
# print("I have %s apples" % 3)
# print("I have %d apples" % 3.5)
# print("I have %i apples" % -3.6)
# print("I have %u apples" % 3.9)
# print("I have %.3f apples" % 3)
# print("I have %x apples" % 3)
# print("I have %e apples" % 3.5)

date_in = (6,9,2025)
date_out = "ngay %02d thang %02d nam %04d" % date_in
print(date_out)
