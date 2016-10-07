LinkedList::LinkedList() {
  _itemCount = 0;
  _head = new Node();
  _last = _head;
}
// Remove and delete all elements first!
LinkedList::~LinkedList() {
  delete _head;
}

uint64_t LinkedList::size() const {
  return itemCount;
}
bool LinkedList::isEmpty() const {
  return (itemCount == 0);
}