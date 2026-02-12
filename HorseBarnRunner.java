/*
 * Activity 3.2.4
 */
import java.util.ArrayList;
public class HorseBarnRunner
{
  public static void main(String[] args)
  {
    /* your code here */
    HorseBarn barn = new HorseBarn();
    ArrayList<Horse> horses = new ArrayList<>();
    horses = barn.getSpaces();
    System.out.println(horses);
    for (Horse h : horses){
      System.out.println(h);
      //if (h.getName().equals("Patches"))
        //horses.remove(h);
      //cant change size of list while iterating over it
    }
    int numSpaces = horses.size();
    ArrayList<Horse> horsesCopy = new ArrayList<>();
    for (Horse h : horses){
      horsesCopy.add(h);
    }
  for (int i = 0; i < numSpaces; i++)
  {
    Horse h = horses.get(i);
    if (h.getName().equals("Patches"))
    {
      System.out.println("Bye bye " +  horses.remove(i));
      numSpaces--;
      i--;
    }
    else if (h.getName().equals("Lady"))
{
    System.out.println("Bye bye " + horses.remove(i));
    numSpaces--;
    i--;
}
  }
  System.out.println(horses);
  numSpaces = horsesCopy.size();
  int j = 0;
  while (j < numSpaces){
    Horse h = horsesCopy.get(j);
        if (h.getName().equals("Patches"))
    {
      System.out.println("Bye bye " +  horsesCopy.remove(j));
      numSpaces--;
      j--;
    }
    else if (h.getName().equals("Lady"))
{
    System.out.println("Bye bye " + horsesCopy.remove(j));
    numSpaces--;
    j--;
}
j++;
  }
  System.out.println(horsesCopy);
      

  }
} 