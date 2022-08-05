import numpy

a = numpy.arange(12).reshape((3, 4))
print(a)
print(numpy.split(a, 2, axis=1))
print(numpy.split(a, 3, axis=0))
print(numpy.array_split(a, 3, axis=1))
print(numpy.vsplit(a, 3))
print(numpy.hsplit(a, 2))
