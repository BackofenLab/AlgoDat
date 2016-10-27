class DynamicArray:
	def __init__(self):
		self.size = 0
		self.elements = []

	def capacity(self):
		return len(self.elements)

	def append(self, item):
		newElements = [0] * (self.size + 1)

		for i in range(0, self.size):
			newElements[i] = self.elements[i]

		newElements[self.size] = item
		self.elements = newElements
		self.size += 1

def test(size):
	a = DynamicArray()
	for i in range(0, size):
		a.append(0)

import timeit

with open('impl1_runtime.csv', 'w') as f:
	f.write("x;y\n")
	for m in range(0, 100):
		m = m * 10
		result = ('%d;%.6f\n' % (m, timeit.timeit('test(' + str(m) + ')', setup='from __main__ import DynamicArray, test', number=5))).replace('.', ',')
		print(result)
		f.write(result)
