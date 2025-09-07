
""" swap list """

list1 = ["anh", "em", "minh", "la", "ban", "be"]


# def swap_list(list):
#     #list1[0], list[-1] = list[-1], list[0]

#     # a,*b,c = list
#     # list = [c,*b,a]

#     first = list.pop(0)
#     last = list.pop(-1)
#     list.insert(0, last)
#     list.append(first)

#     return list

# new_list = swap_list(list1)
# print(new_list)


""" monotonic """
# monotonic = [3,4,7,9,15,17,19]

# tang = False
# giam  = False

# tang = all(monotonic[i] < monotonic[i+1] for i in range(len(monotonic)-1))
# giam = all(monotonic[i] > monotonic[i+1] for i in range(len(monotonic)-1))

# if tang == False and giam == False:
#     print("none-monotonic")
# elif tang == True:
#     print("monotonic tang")
# elif giam == True:
#     print("monotonic giam")

""" Prime Number """

# def is_prime(n):
#     is_prime = True
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             is_prime = False
#             break
#     return is_prime

# for i in range(1,100):
#     if is_prime(i):
#         print(i)

