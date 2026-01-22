/*
 * Activity 3.1.2
 */
public class TraverseBackwards
{
  public static void main(String[] args)
  {    
    int[] goals = {1, 2, 0, 3, 2, 4, 2, 1, 0, 2, 0, 1, 3, 2};
                   
    /* your code here */
    for (int i = 14; (i <= goals.length) && (i != 0); i--){
    System.out.println("Game " + i + ": " + goals[i-1]);
      
      }
    }
  }

