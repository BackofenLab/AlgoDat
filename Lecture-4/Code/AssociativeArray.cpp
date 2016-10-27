#include <unordered_map> // or map

// mapping key: string to value: int
std::unordered_map<std::string, int> age;

if (age.count("Frank") > 0) // check for key
	age.erase("Frank"); // deletes a mapping

age.insert("Bob", 20);

// retrieves a value for key "Bob"
std::cout << "Bob is " << age["Bob"]
	<< " years old" << std::endl;