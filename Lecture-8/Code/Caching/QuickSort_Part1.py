def quicksort(l, start, end):
	if (end - start) < 1:
		return

	i = start
	k = end
	piv = l[start]

	...