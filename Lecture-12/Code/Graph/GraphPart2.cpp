template<typename V>
std::@{\color{cpp_typedef}string}@ @\textbf{Graph<V>::toString}@() {
  std::@{\color{cpp_typedef}ostringstream}@ s, tuples;
  @{\color{cpp_typedef}uint32\_t}@ totalEdges = 0;
  
  for (std::@{\color{cpp_typedef}pair}@<V, std::@{\color{cpp_typedef}vector@}<V>> edges
      : _edges) {
    for (V to : edges.second) {
      ++totalEdges;
      tuples << ", (" << edges.first << ", "
             << to << ")";
    }
  }

  ...