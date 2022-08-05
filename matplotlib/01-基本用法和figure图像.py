import matplotlib.pyplot as plt
import numpy as np

# 输入一个线性方程
x = np.linspace(-1, 1, 50)  # 开头数字是-1，结尾数字是1，中间隔了50个数字
y1 = 2*x + 1
y2 = x**2

# 设置两个figure
plt.figure()
plt.plot(x, y1)

plt.figure(num='figure 02', figsize=(8, 4))  # 长9高9
plt.plot(x, y2)
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')

plt.show()