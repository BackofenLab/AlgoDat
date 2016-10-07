/**
 * @param <V> The type of the vertices
 */
public class Graph<V> {

  protected List<V> vertices;
  protected Map<V, Set<V>> edges;

  public Graph() {
    vertices = new ArrayList<>();
    edges = new TreeMap<>();
  }
  
  ...