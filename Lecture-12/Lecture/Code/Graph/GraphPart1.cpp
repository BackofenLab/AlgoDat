template<typename V> @\textbf{Graph<V>::Graph}@() { }
template<typename V> @\textbf{Graph<V>::\~{}Graph}@() { }

template<typename V>
void @\textbf{Graph<V>::addVertex}@(V vertex) {
  _vertices.push_back(vertex);
}

template<typename V>
void @\textbf{Graph<V>::addEdge}@(V from, V to) {
  _edges[from].push_back(to);
}