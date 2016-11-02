	public long size() {
		return itemCount;
	}

	public boolean isEmpty() {
		return (itemCount == 0);
	}

	public void append(T @{\color{java_variable}value}@) { ... }
	public void insertAfter(Node @{\color{java_variable}cur}@, T @{\color{java_variable}value}@)
		{ ... }
	public void remove(Node @{\color{java_variable}cur}@) { ... }
	public Node get(long @{\color{java_variable}position}@) { ... }
	public boolean contains(T @{\color{java_variable}value}@) { ... }
}