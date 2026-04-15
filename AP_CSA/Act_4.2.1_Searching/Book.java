/*
 * Activity 2.2.7
 *
 * A Book class for the MediaLibrary program
 */
public class Book
{
  private String title;
  private String author;
  private double rating;
    CalendarTest cal = new CalendarTest();

  /*** Constructor ****/
  public Book(String t, String a, double r)
  {
    title = t;
    author = a;
    rating = r;
        cal.modify();

  }
  
   /*** Accessor methods ***/
  public String getTitle() {
    return title;
  }

  public String getAuthor() {
    return author;
  }
  
  public double getRating() {
    return rating;
  }
  public boolean equals(Book b){
      return this.title.equals(b.title) && this.author.equals(b.author);
  }
  public String toString() 
  {
    String info = "\"" + title + "\", written by " + author;
    if (rating != 0) 
    { 
      info += ", rating is " + rating;
    }
    return info;
  }

  /*** Mutator methods ***/
  public void adjustRating(int r){
    double temp = this.rating;
        cal.modify();

    this.rating+=r;
    if ((this.rating > 10 || this.rating<0)){
      this.rating = temp;
    }
    

  }
  public void setTitle(String t) {
    title = t;
        cal.modify();

  }

  public void setAuthor(String a) {
    author = a;
        cal.modify();

  }
  public String getModified(){
  return cal.getModified();
}
public int getChanges(){
  return cal.getAmountChanges();
}
}
