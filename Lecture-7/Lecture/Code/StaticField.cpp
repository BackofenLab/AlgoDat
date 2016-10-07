#include <string>

// Create 10 empty strings stored in "strs"
std::@{\color{cpp_typedef}string}@[] strs = new std::@{\color{cpp_typedef}string}@[10];

// Prints string at index 7 (empty)
std::cout << strs[7] << std::endl;

// Saves the string "Hello World" at index 8
strs[8] = "Hello World";

// Prints string at index 8 ("Hello World")
std::cout << strs[8] << std::endl;