/**
* Adds a new directed edge from one vertex
* to the other.
*/
public Graph<V> addEdge(V from, V to) {
  // If no adjacency-list (set) for the start
  // vertex was created a new one is created
  if (!$\text{\color{java_static}edges}$.containsKey(from)) {
    $\text{\color{java_static}edges}$.put(from, new TreeSet<>());
  }

  // Insert the new edge into the set
  $\text{\color{java_static}edges}$.get(from).add(to);
  return this;
}