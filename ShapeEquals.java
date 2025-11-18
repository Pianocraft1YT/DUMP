/*
 * Activity 1.3.7
*/
public class ShapeEquals
{
  public static void main(String[] args) 
  {
    Shape shape1 = new Shape();
    shape1.setShape("Triangle", 3);
  
    Shape shape2 = new Shape();
    shape2.setShape("Square", 4);
    Shape shape3 = shape1;
    shape3.setShape("Hexagon", 6);
    Shape shape4 = new Shape();
    shape4.setShape("Square", 4);
    Shape shape5 = new Shape();
    shape5.setShape(null, 0);
    System.out.println(shape1.getShape());
    System.out.println("Shape1.equals Shape2? " + shape1.equals(shape2));
    System.out.println("Shape2.equals Shape3? " + shape2.equals(shape3));
    System.out.println("Shape3.equals Shape1? " + shape1.equals(shape3));
    System.out.println("Shape4.equals Shape2? " + shape4.equals(shape2));
    System.out.println("Shape5.equals Shape4? " + shape5.equals(shape4));
  }
}
