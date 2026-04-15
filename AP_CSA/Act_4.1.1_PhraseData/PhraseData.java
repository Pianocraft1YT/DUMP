/*
 * Activity 4.1.1
 */
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;
public class PhraseData
{
  public static void main(String[] args) throws FileNotFoundException {
    File phraseFile = new File("phrases.txt");
    Scanner sc = new Scanner(phraseFile);
    Scanner op = new Scanner(new File("phrases.txt"));
    while (sc.hasNext())
      System.out.println(sc.nextLine());
    
    sc.close();
    // while (op.hasNext())
    //   System.out.println(op.next());
    ArrayList<String> arr = new ArrayList<>();
    while (op.hasNext()){
      String temp = op.next();
      if (!arr.contains(temp))
        arr.add(temp);
    }
    System.out.println((arr));
    for (String e: arr){
      System.out.println(e);
    }
  }
}
