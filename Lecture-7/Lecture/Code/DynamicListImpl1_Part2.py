class DynamicArray:
	...

	def append(self, item):
		newElements = [0] * (self.size + 1)

		for i in range(0, self.size):
			newElements[i] = self.elements[i]

		self.elements = newElements

		newElements[self.size] = item
		self.size += 1