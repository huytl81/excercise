""" Phan loai bang K-mean clustering"""

# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.cluster import KMeans

# df = pd.DataFrame({
#     'x': [12, 20, 28, 18, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53, 55, 61, 64, 69, 72],
#     'y': [39, 36, 30, 52, 54, 46, 55, 59, 63, 70, 66, 63, 58, 23, 14, 8, 19, 7, 24]
# })

# #kmeans = KMeans(n_clusters=3)
# kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)
# kmeans.fit(df)

# # Lấy label và centroid
# labels = kmeans.labels_
# centroids = kmeans.cluster_centers_

# # Vẽ scatter theo cluster
# plt.scatter(df['x'], df['y'], c=labels, cmap='viridis', marker='o')

# # Vẽ centroid
# centroids_x = centroids[:,0]
# centroids_y = centroids[:,1]
# plt.scatter(centroids_x,centroids_y, c=['green', 'red','blue'], marker='X', s=200, label='Centroids')

# plt.title("KMeans Clustering (3 clusters)")
# plt.legend()
# plt.show()

# """ Linear Regression """

from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu
data = pd.read_csv("energy.csv")

# Chuẩn bị bien
temp_x = data['Temperature'].values.reshape(-1, 1)
energy_y = data['Energy'].values.reshape(-1, 1)

# Train Linear Regression
lr = LinearRegression()
lr.fit(temp_x, energy_y)

# Dự đoán
predicted_energy = lr.predict(temp_x)

# In thông tin mô hình
print("Hệ số a (slope):", lr.coef_[0][0])
print("Hệ số b (intercept):", lr.intercept_[0])

# Vẽ dữ liệu + đường hồi quy
plt.scatter(data['Temperature'], data['Energy'], color='blue', label='Thực tế')
plt.plot(data['Temperature'], predicted_energy, label='Predicted Energy')
plt.plot(data['Temperature'], energy_y, label='Hồi quy tuyến tính')
plt.xlabel("Nhiệt độ")
plt.ylabel("Năng lượng tiêu thụ")
plt.title("Linear Regression: Energy vs Temperature")
plt.legend()
plt.show()
