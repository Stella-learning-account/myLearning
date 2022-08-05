import pandas
import numpy

date = pandas.date_range('20220725', periods=6)
df = pandas.DataFrame(numpy.arange(24).reshape((6, 4)), index=date, columns=['A', 'B', 'C', 'D'])

df[df.A > 4] = 0  
# '>' not supported between instances of 'str' and 'int'(使用这个算式时矩阵中只能为‘int’)
# A列中大于4后的行全部改为0
df.iloc[2,2] = 'text'
df.loc['20220729', 'A'] = '***'
df['F'] = numpy.nan
df['E'] = pandas.Series([1, 2, 3, 4, 5, 6], index=pandas.date_range('20220725', periods=6))
print(df)