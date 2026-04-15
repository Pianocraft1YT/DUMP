/*
 * Activity 3.3.3
*/
public class Numbers2D
{
  public static void main(String[] args)
  {
    int[][] numbers = { {1,5,3,8,-3,0,3},
                      {4,4,8,0,3,-1,1}, 
                      {0,3,8,4,-2,7, 6} };
    int sum= 0;
    int totalNum = 0;
    int max = numbers[0][0];
    int min = numbers[0][0];
    int totalNeg = 0;
    for (int[] n : numbers){
      for (int a : n){
        sum+=a;
        totalNum++;
        if (a > max)
          max = a;
        if (a < min)
          min = a;
        if (a < 0)
          totalNeg++;
      }
    }
    System.out.println("Sum: " + sum);
    System.out.println("Average:" + sum*1.0/totalNum*1.0);
    System.out.println("Min: " + min);
    System.out.println("Max: "+ max);
    System.out.println("Total Negative: " + totalNeg);
  }
}
