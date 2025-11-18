import java.util.Scanner;
import java.util.List;
//import Scanner and List functions
public class MadLibs {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    String loop = "yes";
    while (loop.equals("yes")){  
    //Scan for if they want random answers:
    System.out.print("Welcome to the Mad Libs generator!");
    System.out.println(" Would you like random answers? [yes/no]");
    String randomAnswers = scanner.nextLine();
    //confirm their answer
    System.out.println("You said, " + randomAnswers);
    if (randomAnswers.equals("yes") && loop.equals("yes")){ //check if loop is running, account for answers
      int randomLib = (int)(Math.random()*3); //set how many possible libs there are
      if (randomLib == 0) { //first lib
      List <String>possibleVerbs = List.of("Write", "Talk", "Run", "Jump", "Spring", "Eat", "Play"); //list of random verbs
      List <String>possibleAdjectives = List.of("Smart", "Dumb", "Stupid", "Small", "Cute", "Big", "Tiny"); //list of random adjectives
      List <String>possibleNouns = List.of("Banana", "Macbook", "Pencil", "Liver", "Server", "Earring", "Bread"); //list of random nouns
      System.out.println("Gambling Time!"); //lol
      int randomInt = (int)(Math.random()*7); //randomly choose a number
      String newVerb = possibleVerbs.get(randomInt); //select the one it chose
      randomInt = (int)(Math.random()*7);
      String newAdjective = possibleAdjectives.get(randomInt); //repeat, etc
      randomInt = (int)(Math.random()*7);
      String newNoun = possibleNouns.get(randomInt);
      System.out.println("I woke up this morning, feeling so " + newAdjective + "."); //print it
      System.out.println("I needed to find my " + newNoun + ", before I started to " + newVerb);
      randomInt = (int)(Math.random()*7);
      newAdjective = possibleAdjectives.get(randomInt); //reset adjective to new value
      System.out.println("I'm glad I did, or else it would've been " + newAdjective + ".");
      System.out.println("Do you want to try again? yes/no");
      loop = scanner.nextLine(); //restart loop if yes
      }
      if (randomLib == 1) { //next lib
      List <String>possibleVerbs = List.of("Hop", "Zoom", "Accept", "Buzz", "Crack", "Dig", "Fold");
      List <String>possibleAdjectives = List.of("Silly", "Sad", "Bad", "Tanky", "Hard", "Soft", "Odd");
      List <String>possibleNouns = List.of("Bleacher", "Membrane", "Binder", "Disk", "Laptop", "Eye-patch", "Cabbage");
      System.out.println("Gambling Time!");
      int randomInt = (int)(Math.random()*7);
      String newVerb = possibleVerbs.get(randomInt);
      randomInt = (int)(Math.random()*7);
      String newAdjective = possibleAdjectives.get(randomInt);
      randomInt = (int)(Math.random()*7);
      String newNoun = possibleNouns.get(randomInt);
      System.out.println("I needed to go on a " + newAdjective + " to clear my head.");
      System.out.println("My plan was to " + newVerb + " as far as I could before noon.");
      System.out.println("I was trying to find a " + newNoun + ", but I couldn't.");
      System.out.println("Do you want to try again? yes/no");
      loop = scanner.nextLine();
      }
      if (randomLib == 2) { //third lib
      List <String>possibleVerbs = List.of("Sigh", "Joke", "Kick", "Light", "Mug", "Nag", "Park");
      List <String>possibleAdjectives = List.of("Absolute", "Blissful", "Buttery", "Cuddly", "Damp", "Good", "Dirty");
      List <String>possibleNouns = List.of("Air", "Helmet", "Earth", "Drum", "Lip", "Jet", "Pansy");
      System.out.println("Gambling Time!");
      int randomInt = (int)(Math.random()*7);
      String newVerb = possibleVerbs.get(randomInt);
      randomInt = (int)(Math.random()*7);
      String newAdjective = possibleAdjectives.get(randomInt);
      randomInt = (int)(Math.random()*7);
      String newNoun = possibleNouns.get(randomInt);
      System.out.println("I was sitting near a " + newNoun + " when I got a sudden idea.");
      randomInt = (int)(Math.random()*7);
      newNoun = possibleNouns.get(randomInt);
      System.out.println("The idea was to find a " + newAdjective + newNoun + " and steal it.");
      System.out.println("Sadly, my " + newVerb + " was too disturbing, and I lost it.");
      System.out.println("Do you want to try again? yes/no");
      loop = scanner.nextLine();
      }
    }
    else if (randomAnswers.equals("no") && loop.equals("yes")) { //user input mad lib
      System.out.println("No gambling ig..."); //:(
      System.out.println("Which mad lib would you like to try? [1,2,3]"); //3 libs again, custom input
      int madlibInput = scanner.nextInt();
      scanner.nextLine();
      if (madlibInput == 1) { //first lib
      System.out.println("Give me a verb!"); //ask for user input and save it
      String newVerb = scanner.nextLine();
      System.out.println("Give me a adjective!");
      String newAdjective = scanner.nextLine(); //same, etc
      System.out.println("Give me a noun!");
      String newNoun = scanner.nextLine();
      System.out.println("Give me another noun!");
      String newNoun2 = scanner.nextLine();
      System.out.println("I was sitting near a " + newNoun + " when I got a sudden idea."); //print it
      System.out.println("The idea was to find a " + newAdjective + "  " + newNoun2 + " and steal it.");
      System.out.println("Sadly, my " + newVerb + " was too disturbing, and I lost it."); 
      System.out.println("Do you want to try again? yes/no");
      loop = scanner.nextLine();
      }
      else if (madlibInput == 2) { //again lib 2
      System.out.println("Give me a verb!");
      String newVerb = scanner.nextLine();
      System.out.println("Give me a adjective!");
      String newAdjective = scanner.nextLine(); //same old same old
      System.out.println("Give me a noun!");
      String newNoun = scanner.nextLine();
      System.out.println("I needed to go on a " + newAdjective + " to clear my head.");
      System.out.println("My plan was to " + newVerb + " as far as I could before noon.");
      System.out.println("I was trying to find a " + newNoun + ", but I couldn't.");
      System.out.println("Do you want to try again? yes/no");
      loop = scanner.nextLine();
      }
      else if (madlibInput == 3) { //3rd lib
      System.out.println("Give me a verb!");
      String newVerb = scanner.nextLine();
      System.out.println("Give me a adjective!");
      String newAdjective = scanner.nextLine();
      System.out.println("Give me a noun!");
      String newNoun = scanner.nextLine();
      System.out.println("Give me another adjective!");
      String newAdjective2 = scanner.nextLine();
      System.out.println("I woke up this morning, feeling so " + newAdjective + ".");
      System.out.println("I needed to find my " + newNoun + ", before I started to " + newVerb);
      System.out.println("I'm glad I did, or else it would've been " + newAdjective2 + ".");
      System.out.println("Do you want to try again? yes/no");
      loop = scanner.nextLine();
      }
      else{
        System.out.println("You didn't specify 1, 2 or 3."); //account for non-correct answers
        scanner.close();
        break;
      }
    }
    else if (loop.equals("no")) { //end loop
      scanner.close();
      System.out.println("Have a great day!");
      break;
    }
    else{
      System.out.println("You didn't specify yes or no."); //same as above ^
      scanner.close();
      break;
    }

  }

     
  }
  
}
  
 
 