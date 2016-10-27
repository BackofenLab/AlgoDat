class LinkedList:
	def __init__(self):
		self.itemCount = 0
		self.head = Node()
		self.last = self.head

	def size(self):
		return self.itemCount

	def isEmpty(self):
		return self.itemCount == 0