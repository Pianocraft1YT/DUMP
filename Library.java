/*
 * Activity 4.2.1
 *
 * A Library class that stores books
 */
import java.util.ArrayList;
import java.util.Scanner;
import java.io.File;
import java.io.IOException;

/**
 *  A class to prepare a library with books.
 */
public class Library
{
  private ArrayList<Book> childrensBooks = new ArrayList<>();

  /**
   * Constructor for the Library class.
   * Loads data from a text file and populates an ArrayList of Books.
   */
  public Library() throws IOException
  {
      // get data from a file
    Scanner sc = new Scanner(new File("childrensbooksearly1900s.txt"));
    while (true)
    {
      String title = sc.nextLine();
      if (title.equals("")) // end of data
      {
        return;
      }
      
      String author = sc.nextLine();
      // another method from Double class
      double rating = Double.parseDouble(sc.nextLine());
      
      // add the book to the array list
      childrensBooks.add(new Book(title, author, rating));
    }

  }

  /**
   * Returns an ArrayList of childrens books in the library.
   * 
   * @return the ArrayList of childrens books
   */
  public ArrayList<Book> getChildrensBooks()
  {
    return childrensBooks;
  }

}
