/* 
 * Activity 4.1.2
 */
import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class HorseTeams
{
    public static void main(String[] args) throws IOException
    {
      Scanner sc = new Scanner(new File("horsedata.txt"));

      // fixed file size
      for (int i = 0; i < 5; i++) 
      {
        System.out.print("Team " + sc.nextLine() + ": ");
        Horse horse1 = new Horse(sc.next(), sc.nextInt(), sc.nextDouble());
        Horse horse2 = new Horse(sc.next(), sc.nextInt(), sc.nextDouble());
        
        System.out.println(horse1 + " and " + horse2);
      }
    }
}