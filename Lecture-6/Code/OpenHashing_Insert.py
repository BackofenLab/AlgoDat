def insert(s, value):
	j = 0
	
	while t[(h(s) - g(s, j)) mod m] \
			is not None:
		j += 1
	
	t[(h(s) - g(s, j)) mod m] \
		= (s, value)