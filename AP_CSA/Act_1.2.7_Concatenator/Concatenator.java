/*
 * Activity 1.2.7
 */
public class Concatenator
{
   public static void main(String[] args){
  /* Your code here. */
  String wahoo = new String("ME AND YOU");
  String nice = "YOU AND HER";
  System.out.println(nice);
  System.out.println(wahoo);
  String concatIt = wahoo.substring(7);
  String concatItAGAIN = nice.substring(3, 7);
  String concatItAGAINAGAIN = wahoo.substring(6, 10);
  System.out.println(nice.length());
  System.out.println(concatIt + concatItAGAIN + concatItAGAINAGAIN);
   }
}