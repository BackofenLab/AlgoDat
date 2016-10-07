class Graph:
	def __init__(self):
		self.vertices = []
		self.edges = []
	
	def addVertice(self, vert):
		self.vertices.append(vert)
	
	def addEdge(self, fromVert, toVert):
		self.edges.append((fromVert, toVert))
	
	def toString(self):
	return '{'
		+ ', '.join( \
			[str(len(self.vertices)), \
				str(len(self.edges))] \
			+ ["(%s, %s)" % tup \
				for tup in self.edges]) \
		+ '}'