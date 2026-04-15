/*
 * Activity 3.2.4
 *
 * A Horse class to define a horses in a barn.
 */
public class Horse
{
  private String name;
  private int weight;

  /**
   * The constructor for a horse. All horses require
   * a name and their weight. 
   */
  public Horse(String n, int w)
  {
    name = n;
    weight = w;
  }
  /** 
   * Gets the name of the horse.
   * 
   * @return the horse’s name
   * */
  public String getName()
  { 
    return name;
  }
  
  /**
   * Gets the weight of the horse.
   * 
   *  @return the horse’s weight
   */
  public int getWeight()
  {
    return weight;
  }
  
  /**
   * Returns the name of the horse.
   * 
   * @return the horse's name
   */
  public String toString()
  {
    return getName();
  }
}
