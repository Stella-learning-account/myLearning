import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 50)
y1 = 2*x + 1
y2 = x**2

plt.figure(num='figure set:x&y')
line1, = plt.plot(x, y2, label='blue wire:up')
line2, = plt.plot(x, y1, label='red wire:down', color='red', linewidth=1.0, linestyle='--')
plt.legend(handles=[line1,line2], labels=['line1', 'line2'], loc='best')

plt.show()

# 概括：
# 法1: 直接在plt.plot里加label命名线
# 法2:定义一个plt.legend(handles=, labels=, loc='best')
#     并在plt.plot前加上变量名和英文逗号，而后依次在legend里输入变量，定义变量名