def maxSubArray(X, i, j):
	if i == j:							# O(1)
		return (X[i], i, i)				# O(1)
	
	m = (i + j) / 2						# O(1)
	A = maxSubArray(X, i, m)			# T(n/2)
	B = maxSubArray(X, m + 1, j)		# T(n/2)
	
	C1 = rmax(X, i, m)					# O(n)
	C2 = lmax(X, m + 1, j)				# O(n)
	C = (C1[0] + C2[0], C1[1], C2[1])	# O(1)
	
	return max([A, B, C], \				# O(1)
		key=lambda item: item[0])