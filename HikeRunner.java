/*
 * Activity 2.2.5
 */
public class HikeRunner
{
  public static void main(String[] args)
  {
    Hike hike1 = new Hike("Sharp Top", 3.3, 1253);
    System.out.println(hike1);
    Hike hike2 = new Hike("Apple Orchard", 2.6, 1003);
    System.out.println(hike2);
    System.out.println(hike1.compareDifficulty(hike2));
  }
}