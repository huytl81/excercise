import random


so_can_doan = random.randint(1, 100)
so_lan_doan = 5
so_du_doan = None
print("============================================")
print(f"Game doan so tu 1 den 99.")
print(f"Ban co {so_lan_doan} lan doan")
print(f"Toi da sinh ra 1 so ngau nhien.")
print("============================================")

while so_du_doan != so_can_doan and so_lan_doan >= 0:
    so_du_doan = int(input("Nhap so ban doan: "))
    so_lan_doan -= 1
    if so_du_doan > so_can_doan:
        print("So ban doan lon hon so can doan")
    elif so_du_doan < so_can_doan:
        print("So ban doan nho hon so can doan")
    else:
        print("Ban da doan dung so can doan")
        break
    if so_lan_doan == 0:
        print(f"Ban da het so lan doan. So can doan la: {so_can_doan}")
    elif so_lan_doan > 0:
        print(f"Ban con {so_lan_doan} lan doan")