/*
 * Activity 4.2.4
 */
public class SearchAndSort
{ 
  public static void main(String[] args) 
  { 
    final int SIZE = 100000;
    final int find = 7;
    int[] arr = new int[SIZE];
    for (int i = 0; i < SIZE; i++)
      arr[i] = (int)(Math.random() * SIZE) + 1;
    Search.printArray(arr);    
    long startTime = System.nanoTime();

    Search.mergeSort(arr, 0, SIZE-1);
    int loc = SearchAndSort.binarySearch(arr, 0, SIZE-1, find);
    long endTime = System.nanoTime();

    Search.printArray(arr);
    //each for a random array element
    int n = arr[(int)(Math.random() * SIZE)];
    // int result = Search.linearSearch(arr, n, 0); 
     
    System.out.println("Execution time: " +  (endTime - startTime) / 1e6  + " seconds, found " + find + " at index " + loc);
    
    // if (result == -1) 
    //   System.out.println(n + " not found"); 
    // else
    //   System.out.println(n + " found at index  " + result);


  } 
     /**
   * Sorts an array of integers using the merge sort.
   * 
   * @param arr the array of integers to be sorted
   * @param lt  the first index of arr
   * @param rt  the last index of arr
   */
  public static void mergeSort(int arr[], int lt, int rt) 
  { 
    if (lt < rt) 
    { 
      // Find the middle point 
      int m = (lt + rt) / 2; 

      // Sort first and second halves 
      mergeSort(arr, lt, m); 
      mergeSort(arr , m + 1, rt); 

      // Merge the sorted halves 
      merge(arr, lt, m, rt); 
    } 
  } 

  /**
   * A helper method for mergeSort
   *
   * @param arr the array of integers to be merged
   * @param lt  the first index of arr
   * @param m   the midpoint index of arr
   * @param rt  the last index arr
   */
  private static void merge(int arr[], int lt, int m, int rt) 
  { 
    // Find sizes of two subarrays to be merged 
    int n1 = m - lt + 1; 
    int n2 = rt - m; 
    
    // Create temp arrays 
    int left[] = new int[n1]; 
    int right[] = new int[n2]; 
    
    // Copy data to temp arrays
    for (int i = 0; i < n1; ++i) 
      left[i] = arr[lt + i]; 
    for (int j = 0; j < n2; ++j) 
      right[j] = arr[m + 1 + j]; 
    
    /* merge the temp arrays */
    
    // Initial indexes of first and second subarrays 
    int i = 0;
    int j = 0; 
    
    // Initial index of merged subarry array 
    int k = lt; 
    while (i < n1 && j < n2) 
    { 
      if (left[i] <= right[j]) 
      { 
        arr[k] = left[i]; 
        i++; 
      } 
      else
      { 
        arr[k] = right[j]; 
        j++; 
      } 
      k++; 
    } 
    
    // Copy remaining elements of L[] if any
    while (i < n1) 
    { 
      arr[k] = left[i]; 
      i++; 
      k++; 
    } 
    
    // Copy remaining elements of R[] if any 
    while (j < n2) 
    { 
        arr[k] = right[j]; 
        j++; 
        k++; 
    } 
  } 

  /**
   * Print the array
   * 
   * @param arr an array of integers
   */
  public static void printArray(int arr[]) 
  { 
    int n = arr.length; 
    for (int i = 0; i < n; ++i) 
      System.out.print(arr[i] + " "); 
    System.out.println(); 
  } 
   /**
  * Performs a binary search on an array of integers.
  * 
  * preconditions:
  * 
  * @param arr  
  * @param lt   
  * @param rt   
  * @param x    
  * 
  * @return 
  */
  public static int binarySearch(int arr[], int lt, int rt, int x) 
  { 
  if (rt >= lt)
  { 
    int mid = lt + (rt - lt) / 2; 

    if (arr[mid] == x) 
      return mid; 
        
    if (arr[mid] > x) 
      return binarySearch(arr, lt, mid - 1, x); 

    return binarySearch(arr, mid + 1, rt, x); 
  } 
  return -1; 
  } 
} 