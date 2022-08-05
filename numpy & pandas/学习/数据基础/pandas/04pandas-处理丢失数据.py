import pandas
import numpy

date = pandas.date_range('20220725', periods=6)
df = pandas.DataFrame(numpy.arange(24).reshape((6, 4)), index=date, columns=['A', 'B', 'C', 'D'])
df.iloc[0,1] = numpy.nan
df.iloc[1,2] = numpy.nan

print(df)
# 检查数据是否缺失：
print(df.isnull())
# 进化版：
print(numpy.any(df.isnull()) == True)  # 检查是否至少有一个数是缺失的

'''01——
print(df.dropna(axis=0,how='any'))
# axis=0:行;axis=1:列;
# how='any/all'('all'要列/行都为nan的时候才成立)
'''
'''02——
print(df.fillna(value="A"))
'''
