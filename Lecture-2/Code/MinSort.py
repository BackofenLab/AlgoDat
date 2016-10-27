def minsort(elements):
	for i in range(0, len(elements)-1):
		minimum = i
		
		for j in range(i+1, len(elements)):
			if elements[j] < elements[minimum]:
				minimum = j
		
		if minimum != i:
			elements[i], elements[minimum] = \
				elements[minimum], elements[i]
	
	return elements
