if cur == first:
	first = first.nextNode
else:
	pre = first
	while pre.nextNode != cur:
		pre = pre.nextNode
	
	pre.nextNode = cur.nextNode