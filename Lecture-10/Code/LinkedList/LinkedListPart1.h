class LinkedList {
 struct Node {
        int x;
        Node *next;
 };

 private:
  int _itemCount;
  Node _head;
  Node _last;
 
 public:
  LinkedList();
  int size() const;
  bool isEmpty() const;
