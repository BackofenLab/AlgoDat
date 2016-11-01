def maxSubArray(X, i, j):
	if i == j: # trivial
		return (X[i], i, i)
	
	m = (i + j) / 2
	A = maxSubArray(X, i, m)
	B = maxSubArray(X, m + 1, j)
	
	C1 = rmax(X, i, m)
	C2 = lmax(X, m + 1, j)
	C = (C1[0] + C2[0], C1[1], C2[1])
	
	return max([A, B, C], \
		key=lambda item: item[0])