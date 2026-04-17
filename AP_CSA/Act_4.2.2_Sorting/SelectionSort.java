/*
 * Activity 4.2.2
 */
import java.util.ArrayList;
// Add println statements to see the details of the selection sort.

// Show the state of the array at each iteration and the item being sorted.

// Show each change to the array, including the elements that are swapped and their locations in the array.

// When done sorting, show how many times data elements were compared. Do not count looping variables.

// When done sorting, show how many times data in the array was changed.

// 16
// Add println statements to see the insertion details of the insertion sort, repeating the substeps in step 15.

// PLTW
// Computer Science Notebook

// Add to your notes: Selection sort and insertion sort are iterative sorting algorithms that can be used to sort elements in an array or ArrayList.

// Document the number of data comparisons and the number of data changes in each sort.


// 17
// Use a larger ArrayList in each algorithm to compare the performance of the sorting algorithms. Run each sort a few times to get a variety of || results.

// // CODE TO ADD
// for (int n = 0; n < 100 ; n++) {
//   ratings.add((int)(Math.random() * 100));
// }
// PLTW
// Computer Science Notebook

// With a large unordered data set, summarize how the number of data comparisons and the number of data changes between the two sorts.


// 18
// Finally, use a pre-sorted list to compare the performance of the sorting algorithms.

// // CODE TO ADD
// for (int n = 0; n < 100 ; n++) {
//   ratings.add(n);
// }
// PLTW
// Computer Science Notebook

// With an ordered data set, summarize how the number of data comparisons and the number of data changes differ between the sorts.
public class SelectionSort
{
  public static void main(String[] args)
  {
    ArrayList<Integer> ratings = new ArrayList<Integer>();
    ratings.add(5);
    ratings.add(4);
    ratings.add(8);
    ratings.add(9);
    ratings.add(2);
    ratings.add(3);
    ratings.add(1);
    ratings.add(4);
    int comps = 0;
    int swaps = 0;
    int change = 0;
    // iterate through all elements except the last
    for (int i = 0; i < ratings.size() - 1; i++)
    {
      // keeps track of index with smallest value
      int minIndex = i;
      
      // starting at next element, find min value in the list
      for (int j = i + 1; j < ratings.size(); j++)
      {
        // if current value is smaller than the one at minindex,
        // set minIndex to current index
        if(ratings.get(j) < ratings.get(minIndex))
        {
          System.out.println("I found something check it out its kinda small: " + ratings.get(j) + " at index " + j);
          minIndex = j;
        }
        comps++;

      }
      // swap elements if different
      if(ratings.get(i) != ratings.get(minIndex))
      {
        swaps++;
        System.out.println(ratings);
        System.out.println("Here lemme swap " + ratings.get(minIndex) + " with "+ ratings.get(i) + " rq");
        int tmp = ratings.get(i);
        ratings.set(i, ratings.get(minIndex));
        ratings.set(minIndex, tmp);
        System.out.println(ratings+"\n");
        change+=2;
      }
    }
    
    System.out.println(ratings + " Comparisons: " + comps + " Swaps: " + swaps + " Modifications: " + change);
     
  }
}
