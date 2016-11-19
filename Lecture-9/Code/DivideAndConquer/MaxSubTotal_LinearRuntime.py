def maxSubArray(X):
	# sum, start index
	rMax, irMax = 0, 0 # current maximum
	tMax, itMax = 0, 0 # total maximum

	for i in range(len(X)):
		if rMax == 0:
			irMax = i
		
		rMax = max(0, rMax + X[i])
		
		if rMax > tMax:
			tMax, itMax = rMax, irMax
	
	return (tMax, itMax)