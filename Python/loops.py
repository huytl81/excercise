print("============================================")
print("for loop")
print("============================================")

my_for_list = [1,3,5,7,9]

for item in range(len(my_for_list)):
    print(f"Index: {item} => Value: {my_for_list[item]}")

i = 0
for item in my_for_list:
    print(f"Index: {i} => Value: {item}")
    i += 1

print("============================================")
print("break continue")
print("============================================")
for item in my_for_list:
    if item == 5:
        break
    print(item)

for temp in my_for_list:
    if temp == 3:
        continue
    print(temp)

print("============================================")
print("while loop")
print("============================================")

count = 0
while count < 5:
    print("Count:", count)
    count += 1