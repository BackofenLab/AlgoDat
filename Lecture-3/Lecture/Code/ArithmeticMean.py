def arithMean(x):
	a = [0] * len(x)
	for i in range(0, len(x)):
		s = 0
		for j in range(0, i+1):
			s = s + x[j]

		a[i] = s / (i+1)

	return a