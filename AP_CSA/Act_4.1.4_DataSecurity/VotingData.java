/*
 * Activity 4.1.4
 */
import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class VotingData
{ 
  public static void main(String[] args) throws IOException
  { 
    Scanner sc1 = new Scanner(new File("employee.csv"));
    String tokens[];
    
    // iterate over data set 1 with name, age, and ssn
    while (sc1.hasNext()) 
    {
      tokens = sc1.nextLine().split(",");
      String fname = tokens[0];
      String lname = tokens[1];
      int age = Integer.parseInt(tokens[2]);
      String ssn1 = tokens[4];

      // iterate over data set 2 with ssn and state
      Scanner sc2 = new Scanner(new File("state.csv"));
      while (sc2.hasNext()) 
      {
        tokens = sc2.nextLine().split(",");
        String ssn2 = tokens[0];
        String state = tokens[1];

        // show voter's name and their state
        if (ssn2.equals(ssn1) && age >=18)
          System.out.println(fname + " " + lname + " can vote, belonging to " +state);

      }
      
      sc2.close();
    }
    sc1.close();
  }
} 