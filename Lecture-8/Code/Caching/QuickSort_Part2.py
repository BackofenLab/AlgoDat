def quicksort(l, start, end):
	...

	while k > i:
		while l[i] <= piv and i <= end and k > i:
			i += 1
		while l[k] > piv and k >= start and k >= i:
			k -= 1

		if k > i: # swap elements
			(l[i], l[k]) = (l[k], l[i])

	(l[start], l[k]) = (l[k], l[start])
	quicksort(l, start, k - 1)
	quicksort(l, k + 1, end)