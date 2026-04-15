/*
 * Activity 1.3.6
 */
import java.util.Scanner;

public class DeMorgansLawIf
{
  public static void main(String[] args) 
  {
    Scanner sc = new Scanner(System.in);
    
    System.out.println("Enter 'true' or 'false' for A");
    boolean a = sc.nextBoolean(); 

    System.out.println("Enter 'true' or 'false' for B");
    boolean b = sc.nextBoolean();
    
    if (!(a && b))
    {
      System.out.println("NOT (a AND b) evaluates to true");
    }
    else 
    {
      System.out.println("NOT (a AND b) evaluates to false");
    }
    
    /* your code here */
   // !(a||b) --> !a && !b
     if ((a)){
      if((b)){
       System.out.println("Both are true");
      }
      else
      System.out.println("At least one is false");
    }
    
    else if (b)
    System.out.println("One false");
    else
    System.out.println("Both false");
     
     
    if (!(a || b))
    {
      System.out.println("NOT (a OR b) evaluates to true");
    }
    else 
    {
      System.out.println("NOT (a OR b) evaluates to false");
    }
    
     /* your code here */
    
// !(a && b)  --> !a || !b

    if (!a){
      
      if (!b)
      {
        System.out.println("Both are false");
        
      }
      else
        System.out.println("One is false");
    }
  else if (b)
    System.out.println("Both true");
  else
  System.out.println("One true");
    
  }
}
