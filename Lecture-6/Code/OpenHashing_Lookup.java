T lookup(int s) {
	int j = 0;
	
	while (@{\color{java_static}t}@[(h(s) - g(s,j)) % @{\color{java_static}m}@] != null) {
		if (@{\color{java_static}t}@[(h(s) - g(s,j)) % @{\color{java_static}m}@].@{\color{java_static}key}@ == s)
			return @{\color{java_static}t}@[(h(s) - g(s,j)) % @{\color{java_static}m}@].@{\color{java_static}value}@
		
		j++;
	}
	
	return null;
}