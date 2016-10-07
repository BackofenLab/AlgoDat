#include <unordered_map> // or map

// mapping key: string to value: int
std::unordered_map<std::string, int> mymap;

// insert values for key "europe"
mymap["europe"] = 54;

// INSERTS 0 (default value) at key "venus"
if (mymap["venus"] > 0) @\dots@

// only checks if key "venus" is present
if (mymap.count("venus") > 0) @\dots@