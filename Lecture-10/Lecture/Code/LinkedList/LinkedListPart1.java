/**
 * A singly linked list with data type T.
 *
 * @param <T> Data type
 */
public class LinkedList<T> {

	private long itemCount;
	private Node head;
	private Node last;

	public LinkedList() {
		itemCount = 0;
		head = new Node();
		last = head;
	}