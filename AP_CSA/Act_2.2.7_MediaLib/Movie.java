public class Movie{
    private String title;
    private double duration;
    private int rating;
  CalendarTest cal = new CalendarTest();

public Movie(String t, double d, int r){
    title = t;
    duration = d;
    rating = r;
        cal.modify();

}
public String getTitle(){
    return title;
}
public double getDuration(){
    return duration;
}
public int getRating(){
    return rating;
}
public boolean equals(Movie m){
    return this.title.equals(m.title) && this.duration == (m.duration);
}
public String toString(){
    String info = "Movie name: " + this.getTitle() + "\n Duration: " + this.getDuration() + "\n Rating: " + this.getRating();
    return info;
}
public void adjustRating(int r){
    int temp = this.rating;
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

  public void setDuration(double d) {
    duration = d;
        cal.modify();

  }
  public String getModified(){
  return cal.getModified();
}
public int getChanges(){
  return cal.getAmountChanges();
}
}