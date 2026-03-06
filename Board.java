
/** 
 * Activity 3.3.2
 *
 * A game board of NxM board of tiles.
 * 
 */
public class Board
{  
  private static String[] tileValues = {"lion", "lion",
                                        "penguin", "penguin",
                                        "dolphin", "dolphin",
                                        "fox", "fox",
                                        "monkey", "monkey",
                                        "turtle", "turtle"}; 
  int row = 3;
  int collumn = 4;
  private int numGuesses = 0;
  private Tile[][] gameboard = new Tile[row][collumn];

  /**  
   * Constructor for the game. Creates the 2D gameboard
   * by populating it with card values
   * 
   */
  public Board()
  {
    String usedIndexes = "";
    boolean canUse = false;
    int random = (int)(Math.random()*collumn*row);
    for (int i = 0; i < row; i++){
      for (int j = 0; j < collumn; j++){
        while (!canUse){
          random = (int)(Math.random()*collumn*row);
          if (usedIndexes.indexOf("\"" + random + "\",") == -1){
            canUse = true;
          }
        }
        gameboard[i][j] = new Tile(tileValues[random]);
        String temp = "\"" + random + "\",";
        usedIndexes+=temp;
        canUse = false;

      }
    }
  }
//   public Board()
// {
//     int totalTiles = row * collumn;
//     int[] usedIndexes = new int[totalTiles];
//     for (int i = 0; i < totalTiles; i++) {
//         usedIndexes[i] = -1;
//     }
//     int usedCount = 0;
    
//     for (int i = 0; i < row; i++) {
//         for (int j = 0; j < collumn; j++) {
//             int random;
//             boolean alreadyUsed;
//             do {
//                 random = (int) (Math.random() * totalTiles);
//                 alreadyUsed = false;
//                 for (int k = 0; k < usedCount; k++) {
//                     if (usedIndexes[k] == random) {
//                         alreadyUsed = true;
//                         break;
//                     }
//                 }
//             } while (alreadyUsed);
//             usedIndexes[usedCount] = random;
//             usedCount++;
//             gameboard[i][j] = new Tile(tileValues[random]);
//         }
//     }
// }

 /** 
   * Returns a string representation of the board, getting the state of
   * each tile. If the tile is showing, displays its value, 
   * otherwise displays it as hidden.
   * 
   * Precondition: gameboard is populated with tiles
   * 
   * @return a string represetation of the board
   */
  public String toString()
  {
    String output = "";
    int i = 0;
    for (Tile[] row: gameboard){
      for (Tile t: row){
        if (i != 0 && i % collumn == 0)
          if (t.isShowingValue())
            output+=("\n"+ t + " ");
          else
            output+=("\n" + t.getHidden());
        else
          if (t.isShowingValue())
            output+=(t + " ");
          else
            output+=(t.getHidden() + " ");
        i++;
      }
    }
    /* your code here */
    return output;
    }

  /** 
   * Determines if the board is full of tiles that have all been matched,
   * indicating the game is over.
   * 
   * Precondition: gameboard is populated with tiles
   * 
   * @return true if all tiles have been matched, false otherwse
   */
  public boolean allTilesMatch()
  {
    /* your code  here */
    for (Tile[] row: gameboard)
      for (Tile t: row)
        for (Tile[] innerrow:gameboard)
          for (Tile j: innerrow)
            if (!(t.matched() && j.matched()))
              return false;
    return true;
  }

  /** 
   * Sets the tile to show its value (like a playing card face up)
   * 
   * Preconditions:
   *   gameboard is populated with tiles,
   *   row values must be in the range of 0 to gameboard.length,
   *   column values must be in the range of 0 to gameboard[0].length
   * 
   * @param row the row value of Tile
   * @param column the column value of Tile
   */
  public void showValue (int row, int column)
  {
   
    /* your code here */
    int i = 0;
    int currRow = 0;
    int currCol = 0;
    for (Tile[] r: gameboard){
      for (Tile t: r){
        if (i != 0 && i % 4 == 0)
          if (t.isShowingValue() || (currRow == row && currCol == column))
            System.out.print("\n"+ t + " ");
          else
            System.out.print("\n " + t.getHidden());
        else
          if (t.isShowingValue() || (currRow == row && currCol == column))
            System.out.print(t + " ");
          else
            System.out.print(t.getHidden() + " ");
        i++;
        currCol++;
      }
      currCol = 0;
      currRow++;
    }
  }  

  /** 
   * Checks if the Tiles in the two locations match.
   * 
   * If Tiles match, show Tiles in matched state and return a "matched" message
   * If Tiles do not match, re-hide Tiles (turn face down).
   * 
   * Preconditions:
   *   gameboard is populated with Tiles,
   *   row values must be in the range of 0 to gameboard.length,
   *   column values must be in the range of 0 to gameboard[0].length
   * 
   * @param row1 the row value of Tile 1
   * @param col1 the column value of Tile 1
   * @param row2 the row value of Tile 2
   * @param col2 the column vlue of Tile 2
   * @return a message indicating whether or not a match occured
   */
  public String checkForMatch(int row1, int col1, int row2, int col2)
  {
    numGuesses++;
    String msg = "\nWrong.\nGuesses: " + numGuesses;
     /* your code here */
    if (gameboard[row1][col1].equals(gameboard[row2][col2])){
      msg = "\nCorrect.\nGuesses: " + numGuesses;
      gameboard[row1][col1].foundMatch();
      gameboard[row2][col2].foundMatch();
    }
     return msg;
  }

  /** 
   * Checks the provided values fall within the range of the gameboard's dimension
   * and that the tile has not been previously matched
   * 
   * @param row the row value of Tile
   * @param col the column value of Tile
   * @return true if row and col fall on the board and the row,col tile is unmatched, false otherwise
   */
  public boolean validateSelection(int row2, int col2)
  {

    /* your code here */
    
    return (row2 < row && row2 >=0 && col2 >=0 && col2 < collumn && gameboard[row2][col2].matched() == false);
  }
  

}
