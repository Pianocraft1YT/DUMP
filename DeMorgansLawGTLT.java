/*
 * Activity 1.3.6
 */
import java.util.Scanner; 

public class DeMorgansLawGTLT
{
  public static void main(String[] args) 
  {
    Scanner sc = new Scanner(System.in);
    
    System.out.println("Enter a number for X");
    int x = sc.nextInt();

    System.out.println("Enter a number for Y");
    int y = sc.nextInt(); 
    
    
    /* your code here */ 
     if ((x <= 0) || (y <= 0)){
      
    System.out.println("One is negative");
    }
    else
    System.out.println("Both are positive");
    if ((x == 0) || (y == 0)){
      System.out.println("One or more is equal to zero.");
    }
    else
    System.out.println("None are zero");
    





  }
}
