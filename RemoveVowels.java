/*
 * Activity 2.1.3
 */
import java.util.Scanner;

public class RemoveVowels
{
  public static void main(String[] args)
  {
  boolean found = false;
  String vowels = "aeiouy";
  int count = 0;
  String output = "";
  int numTimes = 0;
  Scanner sc = new Scanner(System.in);
  System.out.println("String please: ");
  String input = sc.nextLine().toLowerCase();
  for (int j = 0; j < input.length(); j++){
       String currLetter = input.substring(j,j+1);
       if (vowels.indexOf(currLetter)<=-1){
          output+=input.substring(j,j+1);
        
  }    
}
        
    
   
  System.out.println(output);
}
//get user input
//iterate over input string
    //check if the current char is vowel:  indexOf 
        //  if false add to output
       
       
       
}