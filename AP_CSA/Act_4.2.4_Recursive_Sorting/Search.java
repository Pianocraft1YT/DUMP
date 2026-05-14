
/*
 * Activity 4.2.4
 */

public class Search {
    public static void main(String args[]) {
        String x = "testString";
        int arr[] = { 2, 24, 1, 5, 3, 4, 10, 40, 32, 1, 45, 67 };

        String str = "S";
        int result = linearSearch(x, str, x.length(), 0);

        if (result == -1)
            System.out.println("Could not find " + str);
        else
            System.out.println("Found " + str + " at index " + result);

        int n = 40;
        result = linearSearch(arr, n, 0);

        if (result == -1)
            System.out.println("Could not find " + n);
        else
            System.out.println("Found " + n + " at index " + result);
    }

    public static int linearSearch(String x, String s, int len, int pos) {
        if (pos < len) {
            if (x.substring(pos, pos + 1).equals(s))
                return pos;
            else
                return linearSearch(x, s, x.length(), pos + 1);
        }
        return -1;
    }

    public static int linearSearch(int x[], int n, int pos) {
        if (pos < x.length) {
            if (x[pos] == n)
                return pos;
            else
                return linearSearch(x, n, pos + 1);
        }
        return -1;
    }

   /**
   * Sorts an array of integers using the merge sort.
   * 
   * @param arr the array of integers to be sorted
   * @param lt  the first index of arr
   * @param rt  the last index of arr
   */
    public static void mergeSort(int arr[], int lt, int rt) {
       if (lt < rt) {
           // Find the middle point
           int m = (lt + rt) / 2;

           // Sort first and second halves
           mergeSort(arr, lt, m);
           mergeSort(arr, m + 1, rt);

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
    private static void merge(int arr[], int lt, int m, int rt) {
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
        while (i < n1 && j < n2) {
            if (left[i] <= right[j]) {
                arr[k] = left[i];
                i++;
            } else {
                arr[k] = right[j];
                j++;
            }
            k++;
        }

        // Copy remaining elements of L[] if any
        while (i < n1) {
            arr[k] = left[i];
            i++;
            k++;
        }

        // Copy remaining elements of R[] if any
        while (j < n2) {
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
    public static void printArray(int arr[]) {
        int n = arr.length;
        for (int i = 0; i < n; ++i)
            System.out.print(arr[i] + " ");
        System.out.println();
    }
 
}