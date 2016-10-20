  ...

  public void append(T item) {
    T[] @{\color{java_variable}newElements}@ = new T[size + 1];
    
    // Copy elements to new array
    for (int i = 0; i < size; i++) {
      @{\color{java_variable}newElements}@[i] = elements[i];
    }
    
    elements = @{\color{java_variable}newElements}@;
    size++;
  }
}