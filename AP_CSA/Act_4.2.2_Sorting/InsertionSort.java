/*
 * Activity 4.2.2
 */
import java.util.ArrayList;

public class InsertionSort
{
  public static void main(String[] args)
  {
    ArrayList<Integer> ratings = new ArrayList<Integer>();
    // ratings.add(5);
    // ratings.add(4);
    // ratings.add(8);
    // ratings.add(9);
    // ratings.add(2);
    // ratings.add(3);
    // ratings.add(1);
  //   for (int n = 0; n < 100 ; n++) {
  // ratings.add((int)(Math.random() * 100));
  // }
  for (int n = 0; n < 100 ; n++) {
  ratings.add(n);
}
    int comp = 0;
          int swap = 0;

    // the first element is sorted (so far) so iterate through all others
    for (int i = 1; i < ratings.size(); i++) 
    {
      // save curr element
      int curr = ratings.get(i); 
      
      // store the last element of the sorted portion,
      // the remaining portion is unsorted
      int marker = i - 1; 
      // loop backwards through the sorted portion starting at marker
      while (marker >= 0)
      {      
        if ((curr < ratings.get(marker)))
        {
          System.out.println("Smallest: " + curr);
          System.out.println("At Index: " + marker);
          System.out.println(ratings);
          ratings.set(marker + 1, ratings.get(marker));
          ratings.set(marker, curr); 
          
          System.out.println("Swapped " + ratings.get(marker+1) + " with " + curr);
          System.out.println(ratings+"\n");
          swap++;
        }
        else
        {
          // element is in correct place so stop iterating
          marker = 0;
        }
        comp++;
        marker--;
      }
    }

    System.out.println(ratings + " Swaps: " + swap + " Comparisons: " + comp + " Modifications: " + swap*2);
  }
}
