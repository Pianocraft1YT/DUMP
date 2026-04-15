/*
 * Activity 3.2.3
 */
import java.util.ArrayList;

public class ArrayListExample
{  
   public static void main(String[] args)
   {  
      ArrayList<String> animalList = new ArrayList<String>();  
      animalList.add("Dog");
      animalList.add("Cat");
      animalList.add("Rabbit");
      animalList.add("Frog");
      animalList.add("Horse");
      animalList.add("Cow");
      
      // display list
      System.out.println(animalList);
      
      /* your code here */ 
      animalList.add("Bird");
      animalList.add(3, "Snake");
      System.out.println(animalList.get(2));
      System.out.println(animalList.get(3));
      animalList.remove("Frog");
      // display modified list
      System.out.println(animalList);
      System.out.println(animalList.size());
   }  
}