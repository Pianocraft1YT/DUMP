/**
 * Activity 2.2.7
 * 
 * A MediaLib class for the MediaLibrary program
 */
public class MediaLib
{
  private Book book;

  public void addBook(Book b)
  {
    book = b;
  }
  public Book getBook(){
    return book;
  }
  public String toString() 
  {
    String info = book.getAuthor()+ ", " + book.getTitle();
    
    return info;
  }
  // CODE TO ADD
public void testBook(Book tester){
  tester.setTitle("HAHA");
}


  }
