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
    Player[] players = {new Player("rizz", 10), new Player("wong", 11), new Player("brisa", 13), new Player("hsr", 100)};
    Player[] randPlayers = RandomPermutation.next(players);
    for (Player p: randPlayers){
      System.out.println(p.getName());
    }
    for (Player p : players){
      System.out.println(p.getName());
    }
  }
}