def maxSubArray(X):
	result = (X[0], 0, 0)
	# n loops -> O(n)
	for i in range(0, len(X)):
		# max n loops -> O(n)
		for j in range(i, len(X)):
			# max n loops -> O(n)
			subSum = sum(X[i:j+1])
			if result[0] < subSum: # O(1)
				result = (subSum, i, j)
	return result
