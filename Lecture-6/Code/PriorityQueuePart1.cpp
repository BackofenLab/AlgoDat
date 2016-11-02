#include <queue>
#include <util>
#include <string>

// define entry type alias
typedef std::pair<int, std::string> queue_entry

// define comparator only comparing first element
struct LessByFirst {
  bool operator()(const queue_entry& lhs,
      const queue_entry& rhs) const {
    return lhs.first < rhs.first;
  }
};