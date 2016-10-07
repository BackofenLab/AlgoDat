/*
 * This is free and unencumbered software released into the public domain.
 * Anyone is free to copy, modify, publish, use, compile, sell, or
 * distribute this software, either in source code form or as a compiled
 * binary, for any purpose, commercial or non-commercial, and by any
 * means.
 *
 * In jurisdictions that recognize copyright laws, the author or authors
 * of this software dedicate any and all copyright interest in the
 * software to the public domain. We make this dedication for the benefit
 * of the public at large and to the detriment of our heirs and
 * successors. We intend this dedication to be an overt act of
 * relinquishment in perpetuity of all present and future rights to this
 * software under copyright law.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 * EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
 * MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
 * IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
 * OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
 * ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 * OTHER DEALINGS IN THE SOFTWARE.
 *
 * For more information, please refer to <http://unlicense.org>
 */

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeMap;
import java.util.TreeSet;
import java.util.stream.Collectors;
import java.util.stream.Stream;

/**
 * This class provides a basic interface for storing a graph.
 * Vertices are stored as list and all edges are stored as adjacency list.
 *
 * @param <V> The type of the vertices
 */
public class Graph<V> {

  protected List<V> vertices;
  protected Map<V, Set<V>> edges;

  /**
   * Creates a new empty graph. 
   */
  public Graph() {
    vertices = new ArrayList<>();
    edges = new TreeMap<>();
  }

  /**
   * Adds a new edge from one vertex to the other.
   * 
   * @param vertex The new vertex
   * @return <code>this</code> to follow the builder-pattern
   */
  public Graph<V> addVertex(V vertex) {
    // Just add the vertex to the list
    vertices.add(vertex);
    return this;
  }

  /**
   * Adds a new edge from one vertex to the other.
   * 
   * @param from The start vertex
   * @param to The end vertex
   * @return <code>this</code> to follow the builder-pattern
   */
  public Graph<V> addEdge(V from, V to) {
    // If no adjacency-list (set) for the start vertex was created
    // a new one is created
    if (!edges.containsKey(from)) {
      edges.put(from, new TreeSet<>());
    }

    // Insert the new edge into the set
    edges.get(from).add(to);
    return this;
  }

  @Override
  public String toString() {
    return "{" + Stream.concat(

        // Create a stream using a StreamBuilder
        Stream.builder()
          .add(vertices.size()) // Append the number of vertices
          // Calculate the number of edges
          .add(edges.values().stream().mapToLong(Set::size).sum())
          // Create the stream and transform each element with the
          // toString method into a String object 
          .build().map(Object::toString),

        // Create another stream with the actual edges
        edges.entrySet().stream().flatMap((entry) -> {
          // For each vertex containing a edge extract the key (vertex)
          V key = entry.getKey();
          // Return a string representation of each edge starting from this vertex
          return entry.getValue().stream().map((value) -> ("(" + key + ", " + value + ")"));
      }))
      // Concatenate both streams and separate each element with ", "
      // The result is a String with the format: {|V|, |E|, e1 = (u1, v1), (u2, v2), ...}
      .collect(Collectors.joining(", ")) + "}";
  }
}