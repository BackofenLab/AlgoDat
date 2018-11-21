def maxSubArray(X, i, j): @\onslide<2->@
	if i == j: # trivial case
		return (X[i], i, i)

	# recursive subsolutions for A, B
	m = (i + j) // 2 @\onslide<3->@
	A = maxSubArray(X, i, m)
	B = maxSubArray(X, m + 1, j) @\onslide<4->@

	# rmax and lmax for cornercase C
	C1, C2 = rmax(X, i, m), lmax(X, m + 1, j) 
	C = (C1[0] + C2[0], C1[1], C2[1]) @\onslide<5->@

	# compute solution from results A, B, C
	return max([A, B, C], key=lambda i: i[0])