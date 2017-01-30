class Graph:
	def __init__(self):
		self.vertices = []
		self.edges = []
	
	def add_vertice(self, vert):
		self.vertices.append(vert)
	
	def add_edge(self, fromVert, toVert):
		self.edges.append((fromVert, toVert))
	
	...
