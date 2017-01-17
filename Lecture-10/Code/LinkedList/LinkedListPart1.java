/**
 * A singly linked list with data type int.
 */
public class LinkedList {

	private long itemCount;
	private Node head;
	private Node last;

	public LinkedList() {
		itemCount = 0;
		head = new Node();
		last = head;
	}
