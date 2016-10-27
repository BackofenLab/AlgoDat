import java.util.PriorityQueue;

// only one type parameter
// -> assuming type implements Comparable<T>
PriorityQueue<Integer> q
	= new PriorityQueue<>();

// box int to get unique object
Integer i1 = new Integer(5);
Integer i2 = new Integer(3);

// inserts element i1/i2 into the queue
q.insert(i1);
q.insert(i2);