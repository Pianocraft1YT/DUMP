

public class binarySearch {

    public static void main(String[] args) {
        int[] data = {2, 5, 8, 12, 16, 23, 38}; // Must be sorted
        int target = 23;
        int result = search(data, target);
        
        System.out.println(result != -1 ? "Element found at index: " + result : "Element not found");
    }
    
    /**
    * Returns the index of target if found, else returns -1
    */
    public static int search(int[] arr, int target) {
        int left = 0; //TODO assign to appropriate value
        int right = arr.length; //TODO assign to appropriate value

        while (left <= right) {
            // Use this formula to prevent potential integer overflow
            int mid = (left+right)/2; //TODO assign appropriate, dynamic value

            if (arr[mid] == target) { //TODO replace with appropriate condition
                return mid; // Target found
            } else if (arr[mid] < target) { //TODO replace with appropriate condition
                left = mid+1; //TODO assign to appropriate, dynamic value
            } else {
                right = mid-1; //TODO assign to appropriate, dynamic value
            }
        }
        // Target not found 
        return -1; //TODO assign to appropriate value
    }
}

