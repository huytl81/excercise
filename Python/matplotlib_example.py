

import matplotlib.pyplot as plt
import numpy as np

#NOTE set style
# plt.style.use("ggplot")
plt.style.use("bmh")
#plt.style.use("dark_background")


fig, ax = plt.subplots()
#fig, ax2 = plt.subplots()

# NOTE: line plot
arr_x = np.linspace(0,5,20)
arr_y = np.linspace(0,10,20)
ax.plot(arr_x, arr_y, marker='o', color='red', linewidth=1, linestyle= '-') # truyen day du 2 array
ax.set_xlabel("Truc X")
ax.set_ylabel("Truc Y")
ax.set_title("Title cua Axes nay")
fig.suptitle("Title cua Figure nay", fontsize=18, color="red")
# plt.savefig("my_firstplot.png")

# arr_x = np.array([0,1,2,3,4])
# arr_y = np.array([1,2,3,4,5])
# ax.plot(arr_x,arr_y)

# NOTE: scatter plot
# ax.scatter(arr_x, arr_y, marker="*", color="red")

# NOTE: Histogram plot
#data = np.random.randn(1000)
# ax.hist(data, bins=30, color="green", edgecolor="black", alpha=0.3)

# NOTE: bar plot
# labels = ["class A", "class B", "class C", "class D"]
# counts = [100, 200, 300, 400]
# colors = ["red", "blue", "green", "yellow"]

# ax.bar(labels, counts, color=colors, edgecolor="black", alpha=0.8)

# ax2.barh(labels, counts, color=colors, edgecolor="black", alpha=0.8)

plt.show()