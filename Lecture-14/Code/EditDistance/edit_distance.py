def edit_distance(x, y):
	if len(x) == 0:
		return len(y)
	if len(y) == 0:
		return len(x)

	ed1 = edit_distance(x, y[:-1]) + 1
	ed2 = edit_distance(x[:-1], y) + 1
	ed3 = edit_distance(x[:-1], y[:-1])
	if x[-1] != y[-1]:
		ed3 += 1

	return min(ed1, ed2, ed3)