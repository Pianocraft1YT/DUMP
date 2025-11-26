import java.util.ArrayList;
import java.util.List;

/**
 * Activity 2.2.7
 * 
 * A MediaLib class for the MediaLibrary program
 */
public class MediaLib
{
  CalendarTest cal = new CalendarTest();
  private Movie movie;
  private Book book;
  private Song song;
  List<Book> bookList = new ArrayList<>();
  List<Movie> movieList = new ArrayList<>();
  List<Song> songList = new ArrayList<>();
  private static String owner = "Someone somewhere";
  private static int numEntries;
  public static int getEntries(){
    return numEntries;
  }
  public Song getSong(){
    return song;
  }
  public void addSong(Song s){
    songList.add(s);
    numEntries = movieList.size()+bookList.size()+songList.size();
    cal.modify();
  }
  public static String getOwner(){
    return owner;
  }
  public static void changeOwner(String o){
    owner = o;
  }
  public void addMovie(Movie m){
    movieList.add(m);
    numEntries = movieList.size()+bookList.size()+songList.size();
    cal.modify();
  }
  public Movie getMovie(){
    return movie;
  }

  public void addBook(Book b)
  {
    cal.modify();
    bookList.add(b);
    numEntries = bookList.size() + movieList.size()+songList.size();
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
    for (Song song : songList) {
      if (result.length()> 0) {
        result.append("\n");
      }
      result.append(song.toString());
    }

    return result.toString();
}

   /*String info = book.getAuthor()+ ", " + book.getTitle();
    String movieInfo = movie.getTitle() + ", " + movie.getDuration();
    return movieInfo +"\n"+ info;*/
  
public void testBook(Book tester){
  tester.setTitle("HAHA");
  cal.modify();
}
public String getModified(){
  return cal.getModified();
}
public int getChanges(){
  return cal.getAmountChanges();
}

  }
