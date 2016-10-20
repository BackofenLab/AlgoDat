public class DynamicField<T> {

  private int size;
  private T elements;

  public DynamicField() {
    size = 0;
    elements = T[0];
  }
  
  public int getCapacity() {
    return elements.length;
  }
  
  ...