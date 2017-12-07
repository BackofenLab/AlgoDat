#Alternative trivial case
def maxSubArray(X, i, j): @\onslide<2->@
	# trivial: only one element
	if i == j:
		return (X[i], i, i) @\onslide<3->@

	# trivial: only two elements
	if i + 1 == j:
		return max([
			(X[i], i, i),
			(X[j], j, j),
			(X[i] + X[j], i, j)
		], key=lambda item: item[0])

	... # continue as before
