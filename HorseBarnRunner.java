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
    if (horses.isEmpty()){
      System.exit(1);
    }
    System.out.println(horses);
    for (Horse h : horses){
      System.out.println(h);
      //if (h.getName().equals("Patches"))
        //horses.remove(h);
      //cant change size of list while iterating over it
    }
    int numSpaces = horses.size();
    ArrayList<Horse> horsesCopy = new ArrayList<>();
    ArrayList<Horse> horsesCopyCopy = new ArrayList<>();
    
    for (Horse h : horses){
      horsesCopyCopy.add(h);
      horsesCopy.add(h);
    }
    System.out.println(horsesCopyCopy.size());
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

      System.out.println(barn.horseWeightSort());
    for (int i = 0; i < horsesCopyCopy.size(); i++){
      if (horsesCopyCopy.get(i).getName().equals("Duke")){
        horsesCopyCopy.remove(i);
        horsesCopyCopy.add(i, new Horse("Princess", 1445));
      }
      if (horsesCopyCopy.get(i).getName().equals("Silver")){
        horsesCopyCopy.add(i+1, new Horse ("Chief", 1505));
      }
      if (horsesCopyCopy.get(i).getName().equals("Buddy")){
        horsesCopyCopy.add(i+1, new Horse("Gypsy", 1335));
        System.out.println(horsesCopyCopy);
        horsesCopyCopy.add(i, new Horse("Magic", 1425));
        i++;
      }
    }
    System.out.println(horsesCopyCopy);
  }
} 