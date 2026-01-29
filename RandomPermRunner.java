/*
 * Activity 3.1.4
 */
public class RandomPermRunner
{
  public static void main(String[] args)
  {
    int[] randNums = RandomPermutation.next(10);
    for (int r : randNums)
    {
      System.out.println(r);
    }
    
    System.out.println();
    
    String[] str = {"a", "b", "c", "d", "e"};
    String[] randStr = RandomPermutation.next(str);
    for (String r : randStr)
    {
      System.out.println(r);
    }
    
  }
}