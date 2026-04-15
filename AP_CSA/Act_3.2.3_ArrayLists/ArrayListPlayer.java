// CODE TO ADD

import java.util.ArrayList;

public class ArrayListPlayer
{  
  public static void main(String[] args)
  { 
    ArrayList<Player> players = new ArrayList<>();
    players.add(new Player("youtube"));
    players.add(new Player("wahoo", 10));
    players.add(new Player("not really", 15));
    //players.add("My cousin");
    //errors because this is a string not a player object
    System.out.println(players);
    for (Player p : players){
            System.out.println(p.getName());
    }
  }
}