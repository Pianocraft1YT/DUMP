/* 
 * Activity 4.1.2
 */
import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class PracticeSchedule
{
    public static void main(String[] args) throws IOException
    {
      Scanner sc1 = new Scanner(new File("schedule1.csv"));
      int hours = 0;
      int totalHours = 0;
      String str;
      String[] tokens;
      sc1.nextLine();
      int loops = 0;
      while (sc1.hasNext()) {
        str = sc1.nextLine();
        // System.out.println(str);
        // CODE TO ADD
        tokens =  str.split(",");
        System.out.println(tokens[0] + " I practiced " + tokens[1]  + " hours.");
        totalHours+=Integer.parseInt(tokens[1]);
        loops++;
      }
      System.out.println("Total Hours: " + totalHours);
      System.out.println("Average Hours: " + totalHours/loops*1.0);
      sc1 = new Scanner(new File("schedule2.csv"));
      sc1.nextLine();
      Double totalHours1 = 0.0;
      loops = 0;
      while(sc1.hasNext()){
        str = sc1.nextLine();
        tokens = str.split(",");
        totalHours1+=Double.parseDouble(tokens[1]);
        System.out.println(tokens[0] + " had " + tokens[1] + " hours of practice.");
        loops++;
      }
      System.out.println("Total Hours: " + totalHours1);
      System.out.println("Average Hours: " + totalHours1*1.0/loops*1.0);
      sc1.close();
        
    }
}