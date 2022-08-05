import pandas as pd

data = pd.read_csv('python/爬虫/爬虫/02第二章-数据解析与提取/data01.csv')
print(data)
data.to_pickle("python/爬虫/numpy & pandas/学习/数据基础/pandas/电影评分.csv")
