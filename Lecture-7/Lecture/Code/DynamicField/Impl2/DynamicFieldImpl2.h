template<typename T>
class DynamicArray {
 private:
  T* elements;
  @{\color{cpp_typedef}uint32\_t}@ size;
  @{\color{cpp_typedef}uint32\_t}@ memSize;

 public:
  DynamicArray();

  @{\color{cpp_typedef}uint32\_t}@ capacity();
  void append(T item);
}