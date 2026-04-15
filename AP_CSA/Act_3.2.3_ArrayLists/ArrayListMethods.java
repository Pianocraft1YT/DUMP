// CODE TO ADD
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
public class ArrayListMethods
{
    
    public static void main(String[] args) 
  {
    
//     Use the ArrayList and Scanner classes to meet the following requirements. Read through all steps before beginning your program.


// Create a list with at least three String objects.  (Pick a category, then Strings that fit it)
// Example:  
// List<Strings> dunkables = new ArrayList<>();
// dunkables.add("donuts");
// dunkables.add("kids in a pool");
// dunkables.add("RD");
    Scanner sc = new Scanner(System.in);
    List<String> names = new ArrayList<>();
    names.add("Malcolm");
    names.add("Ohio");
    names.add("Tung tung tung sahur");

// Use a while loop to offer user changes to the list; Stop when user chooses to quit.
// During each loop:
    String input = "";
    int index = 0;
    int loopNum = 0;
    while (!(input.equals("q"))){
        loopNum++;
        System.out.println(//
                "" + "Commands: \r\na: add an element to the end of the list\r\n" + //
                        "i: insert an element at a position\r\n" + //
                        "d: remove an element at a position\r\n" + //
                        "r: replace an element at a position\r\n" + //
                        "q: quit the program\r\n");
        System.out.println("Current state: " +"\r\n");
        for (int i = 0; i < names.size();i++){
            System.out.println((i+1)+": " +  names.get(i));
        }
        System.out.println();
        System.out.println("Enter your command: ");
        input = sc.nextLine();
        switch (input) {
            case "a" -> {
                System.out.println("Enter name: ");
                names.add(sc.nextLine());
            }
            case "i" -> {
                System.out.println("Enter position: (starting from 1)");
                // if (!sc.hasNextInt()) { //checks but *does not read/remove* user input
                //     System.out.println("Your input must be a number\n");
                //     sc.nextLine(); //Since it doesn't contain an int, read & discard the line
                //     continue; //Return to top of while loop and repeat user prompt
                // }
                index = sc.nextInt();
                sc.nextLine();
                System.out.println("Enter name: ");
                names.add(index-1, sc.nextLine());
            }
            case "d" -> {
                System.out.println("Enter position: (starting from 1)");
                index = sc.nextInt();
                sc.nextLine();
                names.remove(index-1);
            }
            case "r" -> {
                System.out.println("Enter position: (starting from 1)");
                index = sc.nextInt();
                sc.nextLine();
                names.remove(index-1);
                System.out.println("Enter name: ");
                names.add(index-1,sc.nextLine());
            }
            default -> System.out.println("You said: "+input+", which isn't valid.");
        }
    }

// Display your list contents
//normal print
// Prompt the user for a command (see example text below)
// Use a Scanner object and the nextLine method (and others as necessary) to get the command from the user, plus any necessary follow-up value(s)
// Use ArrayList add, get, set, remove, and/or size methods to perform the user's requested action: 
// a: add an element to the end of the list
//just use .add(input);
// i: insert an element at a position
// .add and a second input for int
// d: remove an element at a position
// .remove and second input for int
// r: replace an element at a position
//remove element at position, insert element at same posisiont
// q: quit the program
// breaks loop

// Enhancements:
// Make the display of your list user-friendly: Print out all items in the list but number them from 1 to n, where n is the size of your list. (Most users are not computer scientists, so they start lists at 1, not 0).  
// Adjust your code accordingly, since user input will be one off from list index
// Repeat user prompts until valid input is obtained
// Validate input by checking for the size of the list when necessary (certain commands)
// Useful additional Scanner method:  hasNextInt() 
// Inside a while loop that is prompting user for a valid position value:
// if (!sc.hasNextInt()) { //checks but *does not read/remove* user input
//     System.out.println("Your input must be a number\n");
//     sc.nextLine(); //Since it doesn't contain an int, read & discard the line
//     continue; //Return to top of while loop and repeat user prompt
// }
// position = sc.nextInt();//Now assured it's an int : Read & assign to variable
// sc.nextLine(); //Clear out trailing newline left behind by nextInt()

  }
}