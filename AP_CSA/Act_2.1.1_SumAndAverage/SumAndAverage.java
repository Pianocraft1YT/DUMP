/*
 * Activity 2.1.1
 */
import java.util.Scanner;

public class SumAndAverage
{
  public static void main(String[] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the number of values to sum and average: ");
    int numValues = sc.nextInt();
    int sum = 0;
    int saveValues = numValues;
    while (numValues > 0){
      // CODE TO ADD


      System.out.println("Enter Number: ");
      int number1 = sc.nextInt();
      if (number1 == 0)
{
  System.out.println("Only non-zero values, please try again.");
  return;
}
      sum += number1;
      numValues--;
    }
    System.out.println("Here is the sum: " + sum);
    System.out.println("Here is your average: " + (sum/saveValues));
    /* 
    primpt user
    get input
    
    
    
    */
    
  }
  
}