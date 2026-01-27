

/*
 * Activity 3.1.4
 */
public class StandardArrayAlgorithms
{

  public static void main(String[] args)
  {
    int[] goals = {1, 2, 0, 3, 2, 4, 2, 1, 0, 2, 0, 1, 3, 2};
    
    int sum = 0;
    for (int i = 0; i < goals.length; i++)
      sum += goals[i];
    
    System.out.println("All goals: " + sum);
    System.out.println("Average Goals: " + (double) sum/goals.length); //average

    //minimum + maximum value
    int small = goals[0];
    int max = goals[0];
    for (int g = 0; g < goals.length-1; g++){
      int check = goals[g];
      if (check < small){
        small = check;
      }
      if (check > max){
        max = check;
      }
      
      
    }
    System.out.println("Min value: " +small);
    System.out.println("Max value: " + max);

    //check values
    // CODE TO ADD
    Player[] players = {new Player("Alex", 12), new Player("Aiden", 13),
                    new Player("Bobbie", 18), new Player("Blaine", 20),
                    new Player("Chris", 15), new Player("Charlie", 15)};
    boolean hasValue = false;
    for (Player p: players){
      if (p.getAge() >= 18){
        hasValue = true;
        break;
      }
      else
        hasValue = false;
    }
    System.out.println("At least one player 18 or older? " + hasValue);

    //all under 21?
    boolean allHasValue = false;
    for (Player p: players){
      if (p.getAge() < 21){
        allHasValue = true;
      }
      else{
        allHasValue = false;
        break;
      }
        
    }
    System.out.println("All can't gamble? " + allHasValue);
    //num 15 year olds
    int found15 = 0;
    for (Player p: players){
    if (p.getAge() == 15){
      found15++;
    }

  }
  System.out.println("Num. 15 year olds: " + found15);

  //pairing up
  for (int i = 0; i < players.length-1; i+=2){
    System.out.println(players[i].getName() + " and " + players[i+1].getName());
  }
  /*Create an array with 6 elements
    Iterate over the array, starting at the beginning
    Set a temp variable to the value of the current element
    Set the current element to the next element
    Set the next element to the value of temp
  */
 
  }
  
  
}