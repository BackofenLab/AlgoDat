/**
* Adds a new vertex.
* 
* @param vertex The new vertex
*/
public Graph<V> addVertex(V vertex) {
  // Just add the vertex to the list
  $\text{\color{java_static}vertices}$.add(vertex);
  return this;
}