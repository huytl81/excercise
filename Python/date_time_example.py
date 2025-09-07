import time
from datetime import date, datetime, timedelta
import calendar
""" ============================== Time ==================================== """
# Thoi gian da troi qua tu 12:00 AM 1/1/1970
# luon tinh bang seconds
# ticks = time.time()
# print(ticks)

# output la tuple structure_time
# now_time_tuple = time.localtime(ticks) # = gmt + 7
# now_gmt_tuple = time.gmtime(ticks)

# print(now_time_tuple)
# print(now_gmt_tuple)

# chuyen thanh string (input phai la tuple structure_time)
# ascii_time = time.asctime(now_time)
# print(ascii_time)
# print(type(ascii_time))

# # dung ctime de input dau vao la sticks
# c_time = time.ctime(ticks)
# print(c_time)
# print(type(c_time))

# truy xuat cac phan tu trong tuple structure_time
# print("day:",now_time[2],"month:",now_time[1],"year:",now_time[0]) # lay theo index cua tuple time.structure_time
# print("day:",now_time.tm_mday,"month:",now_time.tm_mon,"year:",now_time.tm_year) # lay theo thuoc tinh

""" ============================== strftime & strptime ==================================== """

# ham mktime chuyen structure_time thanh ticks
# print(time.mktime(now_time_tuple))
# print(time.mktime(now_gmt_tuple))

# NOTE: ham strftime de format tuple structure_time thanh string
# now_time_tuple = time.localtime()
# print(time.strftime("%Y-%m-%d %H:%M:%S", now_time_tuple))

# NOTE: ham strptime chuyen string thanh tuple structure_time
# my_birth_str = "16/03/1981 20:30:08"
# time.sleep(10)
# print(time.strptime(my_birth_str, "%d/%m/%Y %H:%M:%S"))

""" ============================== Datetime ==================================== """

# hnay = date.today()
# wday = hnay.weekday() # moday = 0, tuesday = 1, wednesday = 2, thursday = 3, friday = 4, saturday = 5, sunday = 6
#now = datetime.now()

# print(hnay)
# print(hnay.year)
# print(hnay.month)
# print(hnay.day)

# print(wday)

# print(now)

""" ============================== timedelta ==================================== """

now = datetime.now()
today = date.today()

# my_birth_str = "16/03/1981 20:30:08"
# my_birth = datetime.strptime(my_birth_str, "%d/%m/%Y %H:%M:%S")

# next_birthday = date(today.year, my_birth.month, my_birth.day)

# if today > next_birthday:
#     next_birthday = date(today.year + 1, my_birth.month, my_birth.day)

# delta = next_birthday - today

# my_event = today + timedelta(days=delta.days)

# print("My event is: ", next_birthday) # my_event


#lich_thang = calendar.month(today.year, today.month)
lich_thang = calendar.month(now.year, now.month)


print(lich_thang)


print(datetime.__doc__)
