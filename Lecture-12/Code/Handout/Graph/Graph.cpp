#include "Graph.h"

#include <string>
#include <sstream>
#include <vector>
#include <map>
#include <utility>

template<typename V> Graph<V>::Graph() { }
template<typename V> Graph<V>::~Graph() { }

template<typename V>
void Graph<V>::addVertex(V vertex) {
  _vertices.push_back(vertex);
}

template<typename V>
void Graph<V>::addEdge(V from, V to) {
  _edges[from].push_back(to);
}

template<typename V>
std::string Graph<V>::toString() {
  std::ostringstream s;
  std::ostringstream tuples;

  uint32_t count = 0;
  for (std::pair<V, std::vector<V>> edges : _edges) {
    for (V to : edges.second) {
      ++count;
      tuples << ", (" << edges.first << ", " << to << ")";
    }
  }

  s << "{" << _vertices.size() << ", " << count << tuples.str() << "}";
  return s.str();
}
