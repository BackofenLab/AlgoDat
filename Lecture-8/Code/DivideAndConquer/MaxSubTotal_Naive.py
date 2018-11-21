def maxSubArray(X):
	# Store sum, start, end
	result = (X[0], 0, 0)
	for i in range(0, len(X)):
		for j in range(i, len(X)):
			subSum = 0
			for k in range(i, j + 1):
				subSum += X[k]
			if result[0] < subSum:
				result = (subSum, i, j)
	return result
