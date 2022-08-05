import numpy

a = numpy.arange(4)
print(a)


'''copy'''
b = a
c = a
d = b
a[0] = 23
print(a)
print(b, b is a)
print(c, c is a)
print(d, d is a)
d[1:3] = [45, 99]
print(a)
print('/////////////////////////////////////////////////////')


# 会关联，怎么办？
'''deep copy'''
b = a.copy()
a[2] = 2
print(b)
print(a)
