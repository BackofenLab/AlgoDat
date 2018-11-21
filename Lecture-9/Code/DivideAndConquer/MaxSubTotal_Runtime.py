def maxSubArray(X, i, j):
	if i == j:							@\onslide<3->@# O(1)@\onslide<1->@
		return (X[i], i, i)				@\onslide<4->@# O(1)@\onslide<1->@
	
	m = (i + j) // 2					@\onslide<5->@# O(1)@\onslide<1->@
	A = maxSubArray(X, i, m)			@\onslide<6->@# T(n/2)@\onslide<1->@
	B = maxSubArray(X, m + 1, j)		@\onslide<7->@# T(n/2)@\onslide<1->@

	C1 = rmax(X, i, m)					@\onslide<8->@# O(n)@\onslide<1->@
	C2 = lmax(X, m + 1, j)				@\onslide<9->@# O(n)@\onslide<1->@
	C = (C1[0] + C2[0], C1[1], C2[1])	@\onslide<10->@# O(1)@\onslide<1->@

	return max([A, B, C], \				@\onslide<11->@# O(1)@\onslide<1->@
		key=lambda item: item[0])
