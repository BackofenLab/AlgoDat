def maxSubArray(X, i, j):
	if i == j: #trivial case
		return (X[i], i, i)	
	m = (i + j) / 2
        #recursive Subsolutions for A,B
	A = maxSubArray(X, i, m)
	B = maxSubArray(X, m + 1, j)
	#rmax and lmax for bordercase C
	C1 = rmax(X, i, m)
	C2 = lmax(X, m + 1, j)
	C = (C1[0] + C2[0], C1[1], C2[1])
	#Solution results from A,B,C
	return max([A, B, C], \
		key=lambda item: item[0])
