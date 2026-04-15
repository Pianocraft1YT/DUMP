/*
 * Activity 3.3.1
 */
public class TileTester
{
  private static String[] tileValues =
  { "lion", "lion",
    "penguin", "penguin",
    "dolphin", "dolphin",
    "fox", "fox",
    "monkey", "monkey",
    "turtle", "turtle" }; 

  public static void main(String[] args)
  {
    System.out.println(tileValues.length);
    int random = (int)(Math.random()*11);
    /* your code here */
    int row = 3;
    int collumn = 4;
    Tile[][] gameboard = new Tile[row][collumn];
    int increment = 0;
    for (int i = 0; i < row; i++){
      for (int j = 0; j < collumn; j++){
        gameboard[i][j] = new Tile(tileValues[increment]);
        increment++;
      }
    }
    for (Tile[] t: gameboard){
      for (Tile j: t){
        System.out.println(j);
      }
    }
  }
}
