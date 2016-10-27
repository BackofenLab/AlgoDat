void insert(int s, T value) {
	int j = 0;
	
	while (@{\color{java_static}t}@[(h(s) - g(s,j)) % @{\color{java_static}m}@] != null)
		j++;
	
	@{\color{java_static}t}@[(h(s) - g(s,j)) % @{\color{java_static}m}@] = value;
}