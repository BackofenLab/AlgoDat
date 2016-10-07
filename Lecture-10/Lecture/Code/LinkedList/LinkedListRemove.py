def remove(self, cur):
	pre = first
	while pre.nextNode != cur:
		pre = pre.nextNode

	pre.nextNode = cur.nextNode
	itemCount -= 1

	if pre.nextNode == None:
		last = pre