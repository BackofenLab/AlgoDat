template<typename V>
class @{\color{cpp_typedef}Graph}@ {
 private:
  std::@{\color{cpp_typedef}vector}@<V> _vertices;
  std::@{\color{cpp_typedef}map}@<V, std::@{\color{cpp_typedef}vector}@<V>> _edges;

 public:
  @\textbf{Graph}@();
  virtual ~@\textbf{Graph}@();

  void @\textbf{addVertex}@(V vertex);
  void @\textbf{addEdge}@(V from, V to);
  std::@{\color{cpp_typedef}string}@ @\textbf{toString}@();
};