/*
 * Activity 4.1.3
 *
 * Recursive binary search for Activity 4.1.3
 */
import java.util.ArrayList;

/**
 * Finds an entry in the data that matches the provided country name.
 * 
 * @param data An ArrayList of GDP objects
 * @param lt The first index of the search, typically starts at 0
 * @param rt The last index of the search, typically starts at one less than the length of the ArrayList
 * @param str The country name to search for
 * 
 * @return Returns the index of the entry in the ArrayList.
 */
public class GDPSearch
{
  public static int find(ArrayList<GDPData> data,  int lt, int rt, String str) 
  {
      if (rt >= lt)
      { 
        int mid = lt + (rt - lt) / 2; 
        
        if (data.get(mid).getCountry().equals(str))
          return mid; 
            
        if (data.get(mid).getCountry().compareTo(str) > 0) 
          return find(data, lt, mid - 1, str); 
        else
          return find(data, mid + 1, rt, str); 
      } 
  
      return -1;
  }
  public static String findAbove(ArrayList<GDPData> data, String country){
    String output = "Not found";
    int index = find(data, 0, data.size(), country);
    if (index != -1){
       output = "";
       double countryGDP = data.get(index).getGdpLast() - data.get(index).getGdpFirst();
    for (int i = 0; i < data.size(); i++){
      if (data.get(i).getGdpLast() - data.get(i).getGdpFirst() > countryGDP){
        double temp = (data.get(i).getGdpLast() - data.get(i).getGdpFirst());
        double temp2 = ((data.get(i).getGdpLast() - data.get(i).getGdpFirst()) - countryGDP);
        output += "\n"+data.get(i).getCountry() + ": " + temp + " Higher by: " + temp2;

      }
    }
    }
    
   
    return output;
  }
}