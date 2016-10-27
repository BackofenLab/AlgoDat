def insertAfter(self, cur, value):
	if cur == last:
		# also update last node
		append(value)
	else:
		# last node is not modified
		cur.nextNode = Node(value, \
			cur.nextNode)
		itemCount += 1