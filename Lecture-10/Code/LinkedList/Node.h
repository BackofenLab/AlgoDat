template <typename T> class Node {
 private:
  T _value;
  Node<T>* _next;
 
 public:
  Node(T value);
  Node(T value, Node<T>* next);
  ~Node();
 
  T getValue() const;
  void setValue(T value);
  
  Node<T>* getNext() const;
  void setNext(Node<T>* next);
};