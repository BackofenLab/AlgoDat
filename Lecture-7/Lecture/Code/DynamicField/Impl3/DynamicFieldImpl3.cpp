void DynamicArray::append(T item) {
  if (size >= memSize) {
    memSize = std::max(size * 2, 1);
    T[] newElements = new T[memSize];
    for (int i = 0; i < size; i++) {
      newElements[i] = elements[i];
    }

    delete[] elements;
    elements = newElements;
  }
  
  elements[size] = item;
  size++;
}