class DynamicArray:
	def __init__(self):
		self.size = 0
		self.elements = []

	def capacity(self):
		return len(self.elements)

	...