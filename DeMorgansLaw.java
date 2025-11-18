/*
 * Activity 1.3.6
 */
import java.util.Scanner;

public class DeMorgansLaw
{
  public static void main(String[] args) 
  {
    Scanner sc = new Scanner(System.in);
    
    System.out.println("Enter 'true' or 'false' for A");
    boolean a = sc.nextBoolean(); 

    System.out.println("Enter 'true' or 'false' for B");
    boolean b = sc.nextBoolean();
    
    /* your code here */
    if (!(a && b ) == (!(a))||(!(b))) {
      System.out.println("Yay");
    }
    if (!(a || b)==(!(a)) && (!(b))){
      System.out.println("Yay");
    }
    else{
      System.out.println("no");
    }
    // close Scanner when done
    sc.close();
  }
}
