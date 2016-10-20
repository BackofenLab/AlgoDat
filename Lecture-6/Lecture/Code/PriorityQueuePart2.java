// retrieves and removes the head
// of this queue
Integer i3 = q.poll(); // i3 == i2

// retrieves, but does not remove the head
// of this queue
Integer i4 = q.peek(); // i4 == i1

// removing with runtime of O(n)
// i2 was already polled (removed)
q.remove(i2);