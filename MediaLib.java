import java.util.ArrayList;
import java.util.List;

/**
 * Activity 2.2.7
 * 
 * A MediaLib class for the MediaLibrary program
 */
public class MediaLib
{
  private Movie movie;
  private Book book;
  List<Book> bookList = new ArrayList<>();
  List<Movie> movieList = new ArrayList<>();
  public void addMovie(Movie m){
movieList.add(m);
  }
  public Movie getMovie(){
    return movie;
  }
  public void addBook(Book b)
  {
    bookList.add(b);
  }
  public Book getBook(){
    return book;
    }
  public String toString() {
    StringBuilder result = new StringBuilder();

    // Append all books
    for (Book book : bookList) {
        if (result.length() > 0) {
            result.append("\n");
        }
        result.append(book.toString());
    }

    // Append all movies, adding a separator if necessary
    for (Movie movie : movieList) {
        if (result.length() > 0) {
            result.append("\n");
        }
        result.append(movie.toString());
    }

    return result.toString();
}

   /*String info = book.getAuthor()+ ", " + book.getTitle();
    String movieInfo = movie.getTitle() + ", " + movie.getDuration();
    return movieInfo +"\n"+ info;*/
  
  // CODE TO ADD
public void testBook(Book tester){
  tester.setTitle("HAHA");
}


  }
