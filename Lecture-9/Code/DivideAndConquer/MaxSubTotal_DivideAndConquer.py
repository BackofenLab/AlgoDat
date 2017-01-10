def maxSubArray(X, i, j): @\onslide<2->@
	if i == j: # trivial case
		return (X[i], i, i)
	m = (i + j) / 2 @\onslide<3->@
        #Solutions for A and B
	A = maxSubArray(X, i, m)
	B = maxSubArray(X, m + 1, j) @\onslide<4->@
        #rmax and lmax for bordercase C
	C1 = rmax(X, i, m)
	C2 = lmax(X, m + 1, j) 
	C = (C1[0] + C2[0], C1[1], C2[1]) @\onslide<5->@
        #Solution is maximum of A,B,C
	return max([A, B, C], \
		key=lambda item: item[0])@\onslide<6->@
        #Simplification: only maximum 
