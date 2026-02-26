/*
 * Activity 3.3.1
 */
public class InitList2D
{
  public static void main(String[] args)
  {
    String[][] board = { {"close", "quarter"},
                        {"moon", "rock"},
                        {"band", "stand"},
                        {"out", "shine"}  }; 
    System.out.println(board[0]);
    
    
    for (int i = 0; i < board.length; i++)

{
for (int j = 0; j < board[0].length; j++)

    {
    if (i == 0 && j == 0)
      board[i][j] = "fourth";
    System.out.println(board[i][j]);
    }


}
    


 }
}
