void DynamicArray::append(T item) {
  T[] newElements = new T[size + 1];

  // Copy elements to new array
  for (int i = 0; i < size; i++) {
    newElements[i] = elements[i];
  }

  delete[] elements;
  elements = newElements;
  size++;
}