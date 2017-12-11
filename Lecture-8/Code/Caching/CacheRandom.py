def init(size):
	"""Creates a randomly ordered dataset."""

	# use system time as seed
	random.seed(None)
	
	# set random order as accessor
	order = [a for a in range(0, size)]
	random.shuffle(order)
	
	# init array with random data
	data = [random.random() for a in order]
	
	return (order, data)