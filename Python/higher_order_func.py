

def cal_sum(nums):
    return sum(nums)

def hof1(my_func, my_list):
    my_sum = my_func(my_list)
    return my_sum

my_result = hof1(cal_sum, [1,2,3,4,5])
# my_result = cal_sum([3,4,5])

print(my_result)

def cal_min(a,b):
    if a < b:
        return a
    return b
def cal_max(a,b):
    if a > b:
        return a
    return b

# def hof2(cal_str,a,b ):
#     if cal_str == "min":
#         return cal_min(a,b)
#     elif cal_str == "max":
#         return cal_max(a,b)

# my_func = hof2("max", 30,80)
# print(my_func)

def hof2(cal_str):
    if cal_str == "min":
        return cal_min
    elif cal_str == "max":
        return cal_max

my_func = hof2("max")
print( my_func(38,83) )