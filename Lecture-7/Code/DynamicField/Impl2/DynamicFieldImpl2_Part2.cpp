void DynamicArray::append(T item) {
  if (size >= memSize) {
    memSize = size + 100;
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