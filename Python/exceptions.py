
import sys

my_custom_error = "So %s nhap vao khong nam trong khoang 1 - 10"
num = int(input("Nhap mot so trong khoang 1 - 10: "))

""" custom exception using raise and assert """

# if num < 1 or num > 10:
#     raise Exception(my_custom_error % num)
#     # raise ValueError(my_custom_error % num)

# assert num >= 1 and num <= 10, my_custom_error % num



""" exception with built-in exceptions """
try:
    # NOTE Dua custom exception vao khoi try/except
    
    # if num < 1 or num > 10:
    #     raise ValueError(my_custom_error % num)

    #assert num >= 1 and num <= 10, my_custom_error % num

    result = 100 / num
except ZeroDivisionError as e:
    print("Khong the chia cho 0: ", e)
except ValueError as e:
    print("Gia tri nhap vao khong hop le: ", e)
except IndexError as e:
    print("Chi so vuot qua gioi han: ", e)
except KeyError as e:
    print("Khong tim thay key trong dictionary: ", e)
except TypeError as e:
    print("Kieu du lieu khong hop le: ", e)
except AttributeError as e:
    print("Thuoc tinh khong hop le: ", e)
except ModuleNotFoundError as e:
    print("Khong tim thay module: ", e)
except ImportError as e:
    print("Khong tim thay module: ", e)
except FileNotFoundError as e:
    print("Khong tim thay file: ", e)
except SyntaxError as e:
    print("Cu phap khong hop le: ", e)
except NameError as e:
    print("Ten khong hop le: ", e)
except IOError as e:
    print("Loi IO: ", e)
except Exception as e:
    sys_err = sys.exc_info()
    print(sys_err)
else:
    print("100 /", num, "=", result)
finally:
    print('Good bye!')