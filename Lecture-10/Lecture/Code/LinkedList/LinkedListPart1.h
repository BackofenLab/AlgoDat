template<typename T>
class LinkedList {
 private:
  uint64_t _itemCount;
  Node<T>* _head;
  Node<T>* _last;
 
 public:
  LinkedList();
  ~LinkedList();
  
  uint64_t size() const;
  bool isEmpty() const;