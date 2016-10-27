...

def toString(self):
	return '{'
		+ ', '.join( \
			[str(len(self.vertices)), \
				str(len(self.edges))] \
			+ ["(%s, %s)" % tup \
				for tup in self.edges]) \
		+ '}'