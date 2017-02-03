def func(data, k):
	n = len(data)
	out = [0 for i in range(0, n-k, 1)]

	for i in range(0, n-k, 1):
		for j in range(0, k, 1):
			out[i] += data[i+j]

	return out