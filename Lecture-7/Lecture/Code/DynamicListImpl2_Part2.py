def append(self, item):
	if self.size >= len(self.elements):
		newElements = [0] * (self.size + 100)

		for i in range(0, self.size - 1):
			newElements[i] = self.elements[i]

		self.elements = newElements

	self.elements[self.size] = item
	self.size += 1


