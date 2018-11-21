#Implementation right maximum
def rmax(X, i, j):
	maxSum = (X[j], j)
	s = X[j]

	# sum up from the upper index going down
	# (from right to left)
	for k in range(j-1, i-1, -1):
		s += X[k]

		if s > maxSum[0]:
			maxSum = (s, k)

	return maxSum
