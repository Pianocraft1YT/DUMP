

/*
 * Activity 2.2.7
 * 
 * The runner for the MediaLib program
 */
public class MediaLibRunner
{
  public static void main(String[] args)
  {
    System.out.println("Welcome to your Media Library");
    MediaLib myLib = new MediaLib();
    Book myBook = new Book("The Lord of the Rings", "Tolkien");
    System.out.println(myBook);
   // System.out.println(myLib);
    myLib.addBook(myBook);
    //System.out.println(myLib);
    System.out.println(myLib);
    int myRating = 10;
    myBook.adjustRating(myRating);
    System.out.println(myBook);
    System.out.println(myRating);
    //myBook.setTitle("Rizz");
    System.out.println(myBook);
    System.out.println(myLib);
Book currBook = myLib.getBook();
//currBook.setTitle("My Favorite Book");
System.out.println("Current book: " + currBook);
System.out.println(myLib);
System.out.println("You have a NEW Library");
MediaLib myLib2 = new MediaLib();

Book newBook = new Book("To Kill a Mockingbird", "Lee");
myLib2.addBook(newBook);
System.out.println(myLib2);
newBook = new Book("1984", "Orwell");
System.out.println(myLib2);
Book testbook = new Book("Nice", "rip");
myLib.testBook(testbook);
System.out.println(testbook);
Book newBookBook = new Book("The Lord of the Rings", "Tolkien");
System.out.println(newBookBook.equals(myBook));
// bad errors System.out.println(newBook.title);
System.out.println(myLib);
myLib.addBook(newBook);
myLib.addBook(newBookBook);
System.out.println(myLib);
MediaLib.changeOwner("skibidi");

System.out.println(MediaLib.getEntries());
Song newSong = new Song("ohio", 1, 10.20);
myLib.addSong(newSong);
System.out.println(myLib);
System.out.println(myLib.getModified());
System.out.println(newBook.getChanges());
  }
}