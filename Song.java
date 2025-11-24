public class Song{
    private String title;
    private int rating;
    private double duration;

public Song(String t, int r, double d){
    title = t;
    rating = r;
    duration = d;
}
public String getTitle(){
    return title;
}
public double getDuration(){
    return duration;
}
public double getRating(){
    return rating;
}
public boolean equals(Song s){
    return this.title.equals(s.title) && this.duration == (s.duration);
}
public String toString(){
    String info = "Song name: " + this.getTitle() + ", duration: " + this.getDuration() + ", rating: " + this.getRating();
    return info;
}
public void adjustRating(int r){
    int temp = this.rating;
    this.rating+=r;
    if ((this.rating > 10 || this.rating<0)){
      this.rating = temp;
    }
}
  public void setTitle(String t) {
    title = t;
  }

  public void setDuration(double d) {
    duration = d;
  }
}