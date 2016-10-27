class Node:
	""" Defines a node of a singly linked
		list.
	"""
	
	def __init__(self, value, nextNode):
		self.value = value
		self.nextNode = nextNode

	def __init__(self, value):
		self.value = value;
		self.nextNode = None
