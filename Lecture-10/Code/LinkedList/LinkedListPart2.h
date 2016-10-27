  uint64_t size() const;
  bool isEmpty() const;
  
  void append(T value);
  void insertAfter(Node<T>* cur, T value);
  void remove(Node<T>* cur);
  
  Node<T>* get(uint64_t position) const;
  bool contains(T value) const;
};