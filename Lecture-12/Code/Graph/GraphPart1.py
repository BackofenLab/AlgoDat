class Graph:
	def __init__(self):
		self.vertices = []
		self.edges = []
	
	def addVertice(self, vert):
		self.vertices.append(vert)
	
	def addEdge(self, fromVert, toVert, cost):
		self.edges.append( \
			(fromVert, toVert, cost))
	
	...
