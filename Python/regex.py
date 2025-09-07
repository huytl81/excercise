import re


print("============================================")
print("Reg Ex")
print("============================================")


# meta characters
""" 
^: dat o dau chuoi mau => cum ky tu sau ^ phai xuat hien dau tien trong chuoi mau
$: dat o cuoi chuoi mau => cum ky tu truoc $ phai xuat hien cuoi trong chuoi mau
.: 1 ky tu bat ky"
*: cum ky tu truoc no xuat hien 0 hoac nhieu lan
+: cum ky tu truoc no phai xuat hien it nhat 1 lan
(): cum ky tu (abcxyz)
?: cum ky tu truoc no xuat hien 0 hoac 1 lan
{n}: cum ky tu ngay truoc no xuat hien dung n lan 
{n,}: cum ky tu ngay truoc no xuat hien it nhat n lan
{,m}: cum ky tu ngay truoc no xuat hien nhieu nhat m lan
{n,m}: cum ky tu ngay truoc no xuat hien tu n den m lan
|: a | b  (abc) | (def) cky tu bat ky nhieu lan nhung phai xuat hien nhieu nhat 1 lan
'\': Dat truoc ky tu dac biet => ky tu thuong
'\d': chu so bat ky 0-9
'\D': ky tu bat ky khong phai la so
'\s': ky tu space hoac tab hoac xuong dong
'\S': ky tu khong phai la space hoac tab hoac xuong dong
'\w': a-z, A-Z, 0-9, _
'\W': ky tu bat ky khong phai la a-z, A-Z, 0-9, _
'\A': tuong duong ^
'\Z': tuong duong $
'\b': bat dau tu trong chuoi, dung voi r"\b"
"\B": o giua hoac ket thuc tu trong chuoi
'[]': [abc] ~ a hoac b hoac c [a-z], [A-Z], [0-9] [a-zA-Z0-9]
'[^]': [^abc] ~ khong phai a hoac b hoac c
'(?i)': ignore case
'(?m)': multi line
'(?s)': dotall

"""
my_str = "Python is a programming language, i love          python"

# match_obj = re.match("hello", my_str)
# print(match_obj)

# search tra ve doi tuong match
# search_obj = re.search("^h", my_str)
# print(search_obj)

# search_obj = re.search("^[abc]", my_str)
# print(search_obj)

# Doi tuong Match
# str = "0243-987345"
# result = re.search("^(\d{4})-(\d{6})$",str)

# print(result.span())
# print(result.string)
# print(result.group(1))
# print(result.group(2))
# print(result.start())
# print(result.end())

# findall_obj = re.findall("python", my_str, re.IGNORECASE)
# print(findall_obj)

# split_obj = re.split("\s", my_str, maxsplit=3)
# print(split_obj)

# replace_obj = re.sub("python", "odoo", my_str, count=2)
# print(replace_obj)

# tra ve 1 iterator cac doi tuong Match
finditer_obj = re.finditer("python", my_str, re.IGNORECASE)
print(finditer_obj)

for match in finditer_obj:
    print(match.span(), match.group())

# if match_obj is not None:
#     print(match_obj.span())
#     print(match_obj.group())
# else:
#     print("No match found.")

# if search_obj is not None:
#     print(search_obj.span())
#     print(search_obj.group())
# else:
#     print("No search found.")




