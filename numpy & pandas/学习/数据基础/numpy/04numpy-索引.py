import numpy

a = numpy.arange(3, 15)
print(a)
print('索引', a[3])

b = numpy.arange(3, 15).reshape((3, 4))
print(b)
print(b.T)
# print(b[3])不成立
print('索引', b[1][2])  # = print(b[1,2])
print('第1行的所有数', b[1, :])
print('第2列的所有数', b[:, 2])
for row in b:  # 循环出行
    print('循环出行:', row)
for column in b.T:
    print('循环出列:', column)
print(b.flatten())
for item in b.flat:
    print('循环出值:', item)
