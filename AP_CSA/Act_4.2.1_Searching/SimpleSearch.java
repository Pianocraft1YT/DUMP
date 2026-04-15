/*
 * Activity 4.2.1
 */
import java.util.Scanner;

public class SimpleSearch
{
  public static void main(String[] args)
  {
    int[] primesUnder50 = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47};
   
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter prime number less than 50: ");
    int num = sc.nextInt();
    
    for(int i = 0; i < primesUnder50.length; i++)
    {
      if (primesUnder50[i] == num)
      {
        System.out.println(num + " is a prime.");
        return;
      }
    }
    for (int i = primesUnder50.length-1; i >=0; i--){
      if (primesUnder50[i] == num){
        System.out.println(num + " is not NOT a prime.");
        return;
      }
      
    }
    for (int i : primesUnder50){
      if (i==num){
        System.out.println(num + " has identified as prime.");
        return;
      }
    }
    
  }
}