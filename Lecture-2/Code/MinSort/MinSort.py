def minsort(lst):
	for i in range(0, len(lst)-1):
		minimum = i

		for j in range(i+1, len(lst)):
			if lst[j] < lst[minimum]:
				minimum = j

		if minimum != i:
			lst[i], lst[minimum] = \
				lst[minimum], lst[i]

	return lst
