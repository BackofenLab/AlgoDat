#Implementation left maximum
def lmax(X, i, j):
	maxSum = (X[i], i)
	s = X[i]

	# sum up from the lower index going up
	# (from left to right)
	for k in range(i+1, j+1):
		s += X[k]

		if s > maxSum[0]:
			maxSum = (s, k)

	return maxSum
