class DynamicArray:
	def __init__(self):
		self.size = 0
		self.elements = []

	def capacity(self):
		return len(self.elements)

	def append(self, item):
		if self.size >= len(self.elements):
			newElements = [0] * (self.size + 100)

			for i in range(0, self.size - 1):
				newElements[i] = self.elements[i]

			self.elements = newElements

		self.elements[self.size] = item
		self.size += 1

def test(size):
	a = DynamicArray()
	for i in range(0, size):
		a.append(0)

import timeit

with open('runtime.csv', 'w') as f:
	for m in range(0, 100):
		m = m * 10
		result = ('%d;%.6f\n' % (m, timeit.timeit('test(' + str(m) + ')', setup='from __main__ import DynamicArray, test', number=5))).replace('.', ',')
		print(result)
		f.write(result)
