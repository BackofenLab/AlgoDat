def minsort(lst):
@
  \tikzmark{minsort_outer_for_start}
@	for i in range(0, len(lst)-1):
		minimum = i
@
  \tikzmark{minsort_inner_for_start}
@
		for j in range(i+1, len(lst)):
@
  \tikzmark{minsort_if_star}
@			if lst[j] < lst[minimum]:
				minimum = j
@
  \tikzmark{minsort_if_end}
  \tikzmark{minsort_inner_for_end}
@
		if minimum != i:
			lst[i], lst[minimum] = \
				lst[minimum], lst[i]
@
  \tikzmark{minsort_outer_for_end}
@
	return lst
