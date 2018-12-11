def quicksort(l, start, end):
	if (end - start) < 1:
		return

	i = start
	k = end
	pivot = l[start]

	# sort smaller and bigger elements
	while k > i:
		while l[i] <= pivot and i <= end and k > i:
			i += 1
		while l[k] > pivot and k >= start and k >= i:
			k -= 1

		if k > i:
			# swap elements
			(l[i], l[k]) = (l[k], l[i])

	# swap pivot into the middle
	(l[start], l[k]) = (l[k], l[start])

	# sort subparts
	quicksort(l, start, k - 1)
	quicksort(l, k + 1, end)