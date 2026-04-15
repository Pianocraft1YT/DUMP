/*
 * Activity 1.3.2
 */
public class IfDivideByZero 
{
  public static void main(String[] args) 
  {
    double prev = 32.50;
    double curr = prev + prev * .05;
    if (curr > prev)
    System.out.println("It's more.");
    if (curr < prev)
    System.out.println("L gambling, lost money");
    if (curr == prev)
    System.out.println("Nothing changed");
    if (curr == 0)
    System.out.println("You lost it all");
    if (curr < 0)
    System.out.println("bro is in debt");
    
  }
}