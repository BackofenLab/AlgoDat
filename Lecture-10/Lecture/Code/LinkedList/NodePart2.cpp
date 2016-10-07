T Node::getValue() const {
  return _value;
}
void Node::setValue(T value) {
  _value = value;
}

Node<T>* Node::getNext() const {
  return _next;
}
void Node::setNext(Node<T>* next) {
  _next = next;
}