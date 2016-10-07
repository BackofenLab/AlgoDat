/**
 * Provides a handle for an inserted queue
 * item. This handle can be used to remove
 * or update the queue item.
 *
 * @param <T> The type of the data
 */
public class PriorityQueueItem<T> {
	// These member variables are
	// package-private
	int key;
	T value;
	int heapIndex;
}