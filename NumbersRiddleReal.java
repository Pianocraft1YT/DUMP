/*
 * Activity 1.1.6
 * Riddle:  
 * "Choose any integer, double it, add 6, divide it in half, 
 *  and subtract the number you started with.  Result: 3"
 */

 public class NumbersRiddleReal {  //NOTE: File name must match this Class name
  
  public static void main(String[] args) {
    //Supply the required test values:
    int zero = 0; 
    int one = 1;
    int positive = 2;
    int negative = -1;
    double posDouble = 3.30;
    double negDouble = -4.20;
    int negDoubleFix = (int)negDouble; //narrows the value to chop off decimal
    int posDoubleFix = (int)posDouble;


    //Now call the doRiddle() method, once for each test value:
    doRiddle(zero);
    doRiddle(one);
    doRiddle(negative);
    doRiddle(positive);
    doRiddle(posDoubleFix);
    doRiddle(negDoubleFix); //Here's an example
    //TODO: The other five
     
  }

  /*
  *  Expects an integer parameter (as required by the riddle)
  *  Performs riddle algorithm 
  */
  public static void doRiddle(int num) {
    //TODO: Add your code here to perform the riddle algorithm
    // (Remember to display each step's result, with explanatory text)
    int orig = num; //saves original value
    System.out.println();
    System.out.println("Your initial value is: " + orig);
    num *= 2; //doubles it
    System.out.println("Now we double it: " + num);
    num += 6; //adds 6
    System.out.println("Now we add 6: " + num);
    num /= 2; //divides it in half
    System.out.println("Now we half that number: " + num);
    num -= orig; //subtracts original value
    System.out.println("Now subtract the original value: " + num);
  }
  
}
  
 
 