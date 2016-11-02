from queue import PriorityQueue

q = PriorityQueue()

e1 = (5, "A") # element with priority 5
q.put(e1); # insert element e1

# remove and return the lowest item
e2 = q.get()

# peek with runtime O(log n)
if not q.empty():
	e3 = q.get()
	q.put(e3)
