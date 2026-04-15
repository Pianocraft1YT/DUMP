/*
 * Activity 2.1.3
 */
import java.util.Scanner;
import java.lang.Math;
public class Dyslexia
{
  public static void main(String[] args)
  {
  boolean found = false;
  
  String trigger = "dbpq";
  String output = "";
  int value = (int)(Math.random()*4);
  Scanner sc = new Scanner(System.in);
  System.out.println("String please: ");
  String input = sc.nextLine().toLowerCase();
  for (int j = 0; j < input.length(); j++){
       value = (int)(Math.random()*4);
       String currLetter = input.substring(j,j+1);
       if (trigger.indexOf(currLetter)>0){
          output+=trigger.substring(value, value+1);
                 value = (int)(Math.random()*4);

       } else
          output+=input.substring(j, j+1);
  }
      
        
    System.out.println(output);

}
        
    
   
}
//get user input
//iterate over input string
    //check if the current char is vowel:  indexOf 
        //  if false add to output
       
       
       
