import numpy

a = numpy.array([1, 1, 1])
b = numpy.array([2, 2, 2])
print(numpy.vstack((a, b)))  # vertical stack
print(numpy.hstack((a, b)))  # horizontal stack
print(numpy.hstack((a[:, numpy.newaxis], b[:, numpy.newaxis])))
print(a[numpy.newaxis, :])
print(numpy.concatenate((a, b, a, b), axis=0))
