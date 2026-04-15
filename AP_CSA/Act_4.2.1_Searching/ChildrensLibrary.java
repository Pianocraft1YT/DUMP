/*
 * Activity 4.2.1
 */
import java.io.IOException;
import java.util.ArrayList;
public class ChildrensLibrary
{
  public static void main(String[] args) throws IOException
  {
    Library lib = new Library();
    double tempRating = 0;
    ArrayList<Book> books = lib.getChildrensBooks();
    for (Book b : books){
      if (b.getAuthor().equals("L. Frank Baum"))
        System.out.println(b);
      if (b.getTitle().equals("Sky Island"))
        tempRating = b.getRating();
    }
    for (Book anotherBook : books){
      if (anotherBook.getRating() >= tempRating && !(anotherBook.getTitle().equals("Sky Island"))){
        System.out.println(anotherBook);
      }
    }
    int tempIndex = 0;
    for (Book finalBook : books){
      if (finalBook.getTitle().substring(0,3).equals("The")){
        System.out.println(finalBook.getTitle() + " is at index " + tempIndex);
      }
      tempIndex++;
    }
  }
}