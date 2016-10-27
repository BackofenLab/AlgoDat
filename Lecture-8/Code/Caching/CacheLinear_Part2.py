def run(param):
	# unpack data
	(order, data) = param
	
	# init the sum value
	s = 0
	
	for index in order:
		s += data[index]
	
	return s