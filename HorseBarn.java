/*
 * Activity 3.2.4
 *
 * A class to store horses in a barn
 */
import java.util.ArrayList;
import java.util.Scanner;
import java.io.File;

public class HorseBarn
{
  // The stalls or spaces in the barn. Each array element holds a reference to the horse
  // that is currently occupying the space.  A null value indicates an empty space.
  private ArrayList<Horse> spaces = new ArrayList<Horse>();

  /**
   * Constructor for the HorseBarn class. Loads data from the horsedata.csv file
   * and populates the ArrayList spaces. If a blank line occurs in the data file,
   * the array element is assigned a value of null to indicate the absense of a horse.
   */
  public HorseBarn()
  {
    // a try is like an if statement, "throwing" an error if the body of the try fails
    try
    {
      Scanner sc = new Scanner(new File("horsedata.csv"));
      // The Scanner method hasNextLine returns true if there is 
      // another line of input
      while (sc.hasNextLine())
      {
        // String method trim removes whitepsace from the beginning
        // and end of strings
        String temp = sc.nextLine().trim();
        if (temp.equals(""))
        {
          // no horse in this stall, add a null entry
          spaces.add(null);
        }
        else
        {  
          // String method split splits this string based on the
          // specified token and returns an array of individual substrings
          String[] tokens = temp.split(",");  
          String name = tokens[0];
          int  weight = Integer.parseInt(tokens[1]);
          
          // add the horse to the array list
          spaces.add(new Horse(name, weight));
        }
      }
    } catch (Exception e) { System.out.println("Error reading or parsing horsedata.csv" + e); }
  }

  /**
   * Returns the current list of spaces in the barn. If a space does not
   * have a horse in it, the element will be null.
   * 
   * @return the ArrayList of spaces
   */
  public ArrayList<Horse> getSpaces()
  {
    return spaces;
  }
  public double getAverageWeight(){
    int totalWeight = 0;
    int numHorses = 0;
    for (Horse h : spaces)
      if (h != null){
        totalWeight+=h.getWeight();
        numHorses++;
      }
    double averageWeight = totalWeight / numHorses;
    return averageWeight;
  }
  public String horseWeightSort(){
    int heaviest = spaces.get(0).getWeight();
    int lightest = spaces.get(0).getWeight();
    String heaviestName = spaces.get(0).getName();
    String lightestName = spaces.get(0).getName();
    for (Horse h: spaces){
      if (h.getWeight() > getAverageWeight())
        System.out.println(h.getName() +", " +  h.getWeight());
      if (h.getWeight() > heaviest){
        heaviest = h.getWeight();
        heaviestName = h.getName();
      }
      if (h.getWeight() < lightest){
        lightest = h.getWeight();
        lightestName = h.getName();
      }
      

    }
    return "\nLightest Horse: " + lightestName + "\nWeight: " + lightest + "\nHeaviest Horse: " + heaviestName + "\nWeight: " + heaviest + "\nAverage Weight: " + getAverageWeight();
  }
  public ArrayList<Horse> next(int len)
   {
      ArrayList<Horse> r = new ArrayList<>(len);
      ArrayList<Horse> p = new ArrayList<>(len);
      
      for (int i = 0; i < len; i++)
        p.add(i,spaces.get(i));
        
      for (int n = len; n > 0; n--)
      {
        int pos = (int) (Math.random() * n);
        r.add(n, p.get(pos));
        p.remove(pos);
        p.add(pos, p.get(n-1));
        
      }
      
      return r;
   }
}