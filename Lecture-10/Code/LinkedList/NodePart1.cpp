Node::Node(T value) : _value(value) { }
Node::Node(T value, Node<T>* next)
    : _value(value), _next(next) { }

Node::~Node() { }