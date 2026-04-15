/*
 * Activity 3.1.4
 *
 * Generate random permutations of integers or strings
 */
public class RandomPermutation
{
  /*
   * Genereates a permutation of random integers. The number of
   * integers to generate is designated by length and the
   * randomized list of integers is returned.
   *
   * Precondition: leng cannot be negative
   * @return a randomized list of length len
   */
   public static int[] next(int len)
   {
      int[] r = new int[len];
      int[] p = new int[len];
      
      for (int i = 0; i < len; i++)
        p[i] = i + 1;
        
      for (int n = len; n > 0; n--)
      {
        int pos = (int) (Math.random() * n);
        r[n-1] = p[pos];
        p[pos] = p[n-1];
      }
      
      return r;
   }
   
   /**
    * Genereate one random permutation of a provided array of strings
    * in parameter seq.
    * A ranomly ordered version of the array is returned.
    *
    * Initial conditions: seq cannot be null
    * @return a randomized list of length seq.length
    */
  public static String[] next(String[] seq)
  {  
    int length = seq.length;
    
    String[] p = new String[length];
    String[] r = new String[length];

    int i = 0;
    for (String s : seq)
    {
      p[i] = s;
      i++;
    }

    for (int n = length-1; n >=0; n--)
      {
        int pos = (int)(Math.random() * n);
        r[n] = p[pos];
        p[pos] = p[n];
      }
      // debug: for (String tmp : r) System.out.println(tmp);
      return r;
    }

  public static Player[] next(Player[] p){
    int length = p.length;
    int max = p.length-1;
    Player[] result = new Player[length];
    Player[] copy = new Player[length];
    int j = 0;
    for (Player i: p){
      copy[j] = i;
      j++;
    }
    for (int i=0; i < copy.length; i++){
      int rand = (int)(Math.random()*max);
      Player temp = copy[rand];
      copy[rand] = copy[copy.length-1-i];
      max--;
      
      result[i] = temp;
    }
    return result;
  }

}
