/**
 * Activity 2.2.7
 * 
 * A MediaLib class for the MediaLibrary program
 */
public class MediaLib
{
  private Movie movie;
  private Book book;

  public void addMovie(Movie m){
    movie = m;
  }
  public Movie getMovie(){
    return movie;
  }
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
    String movieInfo = movie.getTitle() + ", " + movie.getDuration();
    return movieInfo +"\n"+ info;
  }
  // CODE TO ADD
public void testBook(Book tester){
  tester.setTitle("HAHA");
}


  }
