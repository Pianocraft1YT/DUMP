/*
 * Activity 3.3.1
 */
public class Traversing2DArrays
{
  public static void main(String[] args)
  {
   String[][] board = { {"close", "quarter"},
                        {"moon", "rock"},
                        {"band", "stand"},
                        {"out", "shine"} }; 
                       
    /* your code here */
  for (String[] row: board){
      for (String collumn: row){
        System.out.println(collumn);
      }
    }
    for (String[] row: board){
      for (String collumn: row){
        // collumn = "Test"; this doesnt change the array at all
        System.out.print(collumn + "\t");
      }
      System.out.println();
    }
  }
}
