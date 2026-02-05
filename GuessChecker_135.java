/*
 * Activity 1.3.2 & 3
 */
import java.util.Scanner;
 
public class GuessChecker_135
{
  static Scanner sc = new Scanner(System.in);

	public static void main(String[] args)
	{
    /* Add any variables you will need throughout the program here. */
    
    // Generate a random number
    int targetNumber = getRandomNumber();
    //System.out.println(targetNumber);  // uncomment for debugging
    
    // Break the random number into four variables.
    int r1 = targetNumber / 1000;
    int r2 = targetNumber / 100 % 10;
    int r3 = targetNumber / 10 % 10;
    int r4 = targetNumber % 10;
    
    // Get the user's guess
    
    //System.out.println(guess);   // uncomment for debugging
    
    // Break the user's guess into four variables.
    

    /*your code here*/
    boolean correct = false;
    int nearMiss = 0;
    while (!correct){
    int guess = getGuess();
    int g1 = guess / 1000;
    int g2 = guess / 100 % 10;
    int g3 = guess / 10 % 10;
    int g4 = guess % 10;
    if (guess == targetNumber){
    System.out.println("You got it!");
    correct = true;
    System.out.println("You had " + nearMiss + " near guesses.");
    break;
    }
    if (g1 == r1)
    System.out.println("You got the first digit!");
    else if ((g1 + 1 == r1) || (g1 -1 == r1)){
    System.out.println("You are one off for the first digit.");
    nearMiss++;}
    else
    System.out.println("First digit is wrong.");
    if (g2 == r2)
    System.out.println("You got the second digit!");
    else if ((g2 +1 == r2) || (g2 -1 == r2)){
    System.out.println("You are one off for the second digit.");
    nearMiss++;
    }
    else
    System.out.println("Second digit is wrong.");
    if (g3 == r3)
    System.out.println("You got the third digit!");
    else if ((g3 +1 == r3 ) || (g3 - 1 == r3)){
    System.out.println("You are one off for the third digit.");
    nearMiss++;
    }
    else 
    System.out.println("Third digit is wrong.");
    if (g4 == r4)
    System.out.println("You got the fourth digit!");
    else if ((g4 + 1 == r4) || (g4 -1 == r4)){
          System.out.println("You are one off from the fourth digit.");
nearMiss++;
    }
    else
    System.out.println("Fourth digit is wrong.");

    }
    
    // close Scanner when done
    sc.close();
	}
  // Checks to ensure no duplicate digits in a int.
	public static boolean hasDupes(int num)
	{ 
		boolean[] digs = new boolean[10];
		while (num > 0)
		{
			if (digs[num % 10])
			  return true;
			digs[num % 10] = true;
			num /= 10;
		}
		return false;
	}

  // Creates a new random 4 digit code 1000-9999 with no duplicates.
  public static int getRandomNumber() 
  { 
		int target = (int) (Math.random() * 9000 + 1000);
		while (hasDupes(target))
		  target = (int) (Math.random() * 9000 + 1000);
    return target;
  }

  // Prompts the user for a guess and repeats until valid guess is made.
  public static int getGuess()
  { 

    int userGuess = 0;
    boolean validGuess = false;
    
    while (!validGuess)
    {
      System.out.print("Guess a 4-digit number from 1000 to 9999 with no duplicate digits: ");
      userGuess = sc.nextInt();
      if (!(hasDupes(userGuess) || (userGuess < 1000))) 
        validGuess = true;
    }
    return userGuess;
  }
}
