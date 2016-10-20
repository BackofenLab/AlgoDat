template<typename T>
class DynamicArray {
 private:
  T* elements;
  @{\color{cpp_typedef}uint32\_t}@ size;

 public:
  DynamicArray();

  uint32_t capacity();
  void append(T item);
}