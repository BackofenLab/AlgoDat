	/**
	 * Creates a new node with a next node
	 * assigned.
	 */
	public Node(T @{\color{java_variable}value}@, Node<T> @{\color{java_variable}next}@) {
		this.value = @{\color{java_variable}value}@;
		this.next = @{\color{java_variable}next}@;
	}
	/**
	 * Creates a new node without a next
	 * node assigned.
	 */
	public Node(T @{\color{java_variable}value}@) {
		this.value = @{\color{java_variable}value}@;
		this.next = null;
	}