#include <string>
#include <vector>

std::@{\color{cpp_typedef}vector}@<std::@{\color{cpp_typedef}string}@> words;

words.push_back("Hello");
words.push_back("World");

// Prints string at index 0 ("Hello")
std::cout << words[0] << std::endl;

words.resize(1);  // Keep the first word
words.clear();  // Remove all elements