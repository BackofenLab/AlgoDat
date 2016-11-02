
#ifndef GRAPH_H_
#define GRAPH_H_

#include <vector>
#include <map>
#include <string>

template<typename V>
class Graph {
 private:
  std::vector<V> _vertices;
  std::map<V, std::vector<V>> _edges;

 public:
  Graph();
  virtual ~Graph();

  void addVertex(V vertex);
  void addEdge(V from, V to);
  std::string toString();
};

#endif /* GRAPH_H_ */
