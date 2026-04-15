/*
 * Activity 3.3.3
*/

import java.util.Arrays;

public class Names2D
{
  public static void main(String[] args)
  {
    String[][] names = {{"Ari", "Avery", "Ash", "Aman"},
                        {"Brynn", "Bodie", "Bo", "Barrie"},
                        {"Cris", "Carter", "Cali", "Ari"}};
    boolean hasDupes = false;
    for (String[] row : names){
      for (String name: row){
        for (String[] row1 : names)
          for (String nameToCheckAgainst: row1){
            if (name.equals(nameToCheckAgainst))
              hasDupes = true;
          }
      }
    }
    System.out.println("Determine if there are duplicate names: " + hasDupes);
    for (int i = 0; i < names.length; i++){
      for (int j = 0; j < names[i].length-1; j++){
        System.out.println(names[i][j] + " and " + names[i][j+1]);
        j++;
      }
    }

    for (int i = 0; i < names.length; i++){
      for (int j = names[i].length-1; j > -1; j--){
        if (i ==1){
          System.out.println(names[i][j]);
        }
      }
    }    
    String temp3 = names[0][0];

    System.out.println("\nAccess consecutive pairs of elements in each row:");
    // for (int i = 0; i < names.length; i++){
    //   for (int j = 0; j < names[i].length-1; j++){
    //     names[i][j] = names[i][j+1];
    //   }
    // }
    // names[2][3] = temp3;
    // System.out.println(Arrays.deepToString(names));
    for (int i = 0; i < names[0].length-1;i++){
      names[0][i] = names[0][i+1];
    }
    names[0][2] = temp3;
    System.out.println(Arrays.deepToString(names));
    for (int i = 0; i < names.length-1; i++){
      for (int j = 0; j < names[i].length; j++){
        if (j == 2){
          names[i][j] = names[i+1][j];
        }
      }
    }
    names[2][2] = temp3;
    System.out.println(Arrays.deepToString(names));
    // String temp = names[0][names[0].length-1];
    // names[0][names[0].length-1] = names[2][names[2].length-1];
    // names[2][names[2].length-1] = temp;
    // System.out.println(Arrays.deepToString(names));


    System.out.println("\nReverse the order of the elements in second column:");
    
    
    System.out.println("\nShift an element in a row: Shift the first name in the first row left to the last name in the row:");
   
   
    System.out.println("\nShift an element in a column: Shift the last name in the first row down to the last row:");
   
  }
}
