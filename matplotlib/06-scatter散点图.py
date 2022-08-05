import matplotlib.pyplot as plt
import numpy as np

n = 1024    # data size 数据量
X = np.random.normal(0, 1, n)  # n个0-1之间的数
Y = np.random.normal(0, 1, n)
T = np.arctan2(Y, X)    # for color later on 随机上色

plt.scatter(X, Y, s=75, c=T, alpha=.5)  # c-颜色

plt.xlim(-1.5, 1.5)
plt.xticks(())  # ignore xticks
plt.ylim(-1.5, 1.5)
plt.yticks(())  # ignore yticks

plt.show()

# 一条线的散点图
plt.scatter(np.arange(5), np.arange(5))
plt.show()