#Implementation - linear runtime
def maxSubArray(X):@\onslide<2->@
	# sum, start index
	rMax, irMax = 0, 0 # current maximum
	tMax, itMax = 0, 0 # total maximum
        @\onslide<3->@
	for i in range(len(X)):
		if rMax == 0:
			irMax = i
		rMax = max(0, rMax + X[i])
		@\onslide<4->@
		if rMax > tMax:
			tMax, itMax = rMax, irMax

	return (tMax, itMax)
