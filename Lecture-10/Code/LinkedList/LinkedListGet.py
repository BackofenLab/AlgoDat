def get(self, pos):
	if pos < 0 or pos >= itemCount:
		return None

	cur = head
	for i in range(0, pos):
		cur = cur.nextNode

	return cur