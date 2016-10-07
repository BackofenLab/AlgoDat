def contains(self, value):
	cur = head
	
	for i in range(0, itemCount):
		cur = cur.nextNode
		if cur.value == value:
			return true

	return false