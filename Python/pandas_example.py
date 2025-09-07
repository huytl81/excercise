import pandas as pd
import numpy as np

# NOTE: Doc file
# data = pd.read_csv("my_data.csv")

# print(data)
# print(type(data))

# print(data.head(3))
# print(data.tail(2))

# print(data.info())
# print(data.describe())

# print(data.columns)
# print(data.index)

# print(data[["Name", "Age"]])
# print(data.Name)

# NOTE: Luu file
# data.to_csv("my_new_data.csv", index=False) # index la chi so row


""" DataFrame chuyen data dang dict sang excel, csv"""
# df = pd.DataFrame({
#     "ID": [1, 2, 3, 4],
#     "Name": ["Nguyen Van A", "Tran Van B", "Nguyen Thi C", "Nguyen Van D"],
#     "Age": [20, 21, 22, 23],
#     "Address": ["Ha Noi", "Hai Phong", "HCM", "Da Nang"],
#     "Gender": ["Nam", "Nu", "Nam", "Nu"]
# })

# df.set_index("ID")

# print(df)
# print(df.columns)
# print(df.index)

""" ======== iloc va loc ============ """

# print(df.loc[0]) # lay hang 0
# print(df.loc[[0,2]]) # lay hang 0 va hang 2
# print(df.loc[3,2]) ==> Loi

# lay tat ca cac hang va chi lay cot Name chua "Nguyen Van"
# print(df.loc[df["Name"].str.contains("Nguyen Van")])

# lay tat ca cac hang cot Name va Address
# print(df.loc[:, ["Name", "Address"]])

#print(df.iloc[0])
#print(df.iloc[[0,2]])
#print(df.iloc[3,2])
#print(df.iloc[:, [0,2]])

# new_df = df.set_index("Name")
# print(new_df)

""" ======== select, filter ============ """
# filtered = df["Age"] > 21
# print(df.loc[filtered, ["Name", "Age"]])

# # them cot Country
# df["Country"] = ["Viet Nam", "Viet Nam", "Viet Nam", "Viet Nam"]
# print(df)

# # xoa cot Gender

# df_gender_dropped = df.drop("Gender", axis=1)

# print(df_gender_dropped)

# # uupdate gia tri 1 cell

# df.loc[1, "Name"] = "Odoo Lover"
# print(df)

""" ======== NaN ============ """

# df["Salary"] = [50000, None, 70000, 100000]
# print(df)

# df["Salary"] = df["Salary"].fillna(0)

# new_df = df.dropna()
# print(new_df)


""" reshape & reave """
# duoi du lieu thanh 1 hang
# data = pd.read_csv('my_data.csv')
# print(data.values.ravel())

# duoi du lieu theo so hang va so cot
# data = pd.read_csv('my_data.csv')
# print(data.values.reshape(-1, 20))
