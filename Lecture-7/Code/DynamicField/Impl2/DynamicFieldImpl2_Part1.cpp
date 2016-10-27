DynamicArray::DynamicArray()
  : size(0), memSize(0), elements(nullptr) {}

@{\color{cpp_typedef}uint32\_t}@ DynamicArray::capactity() {
  return size;
}