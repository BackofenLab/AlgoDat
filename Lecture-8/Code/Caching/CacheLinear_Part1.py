def init(size):
	"""Creates the dataset."""

	# use system time as seed
	random.seed(None)
	
	# set linear order as accessor
	order = [a for a in range(0, size)]
	
	# init array with random data
	data = [random.random() for a in order]
	
	return (order, data)