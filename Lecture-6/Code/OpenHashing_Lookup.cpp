T lookup(int s)
{
  int j = 0;

  while (@{\color{cpp_static}t}@[(h(s) - g(s,j)) % @{\color{cpp_static}m}@]) {
    if (@{\color{cpp_static}t}@[(h(s) - g(s,j)) % @{\color{cpp_static}m}@].@{\color{cpp_static}key}@ == s)
      return @{\color{cpp_static}t}@[(h(s) - g(s,j)) % @{\color{cpp_static}m}@].@{\color{cpp_static}value}@

    j++;
  }  // end while

  return nullptr;
}