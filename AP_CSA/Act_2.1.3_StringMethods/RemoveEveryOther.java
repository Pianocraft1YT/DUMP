/*
 * Activity 2.1.3
 */
import java.util.Scanner;

public class RemoveEveryOther
{
  public static void main(String[] args)
  {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter a String: ");
    String input = sc.nextLine();
    String output = "";
    
    /* your code here */
    for (int i = 0; i < input.length(); i++){
      output += input.substring(i, i+ i%2);
  
    }
    System.out.println(output);
  }   
}