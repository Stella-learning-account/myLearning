from cProfile import label
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

# plot data

# Series
data = pd.Series(np.random.randn(1000),index=np.arange(1000))
data = data.cumsum()
# data.plot()
# plt.show()

# DataFrame
data = pd.DataFrame(np.random.randn(1000,4),
                    index=np.arange(1000),
                    columns=list('ABCD'))
data = data.cumsum()
print(data.head())
# data.plot()
# plot methods : 'bar','box','kde','area','scatter','hexbin','pie'
ax = data.plot.scatter(x='A',y='B',color='DarkGreen',label='text_map')
data.plot.scatter(x='A',y='D',color='brown',label='text_map2',ax=ax)  # 只能用ax来表示
plt.show()