  ...

  public void append(T @{\color{java_variable}item}@) {
    T[] @{\color{java_variable}newElements}@ = new T[size + 1];
    
    // Copy elements to new array
    for (int @{\color{java_variable}i}@ = 0; @{\color{java_variable}i}@0< size; @{\color{java_variable}i}@++) {
      @{\color{java_variable}newElements}@[@{\color{java_variable}i}@] = elements[@{\color{java_variable}i}@];
    }
    
    elements = @{\color{java_variable}newElements}@;
    elements[size] = @{\color{java_variable}item}@;
    size++;
  }
}