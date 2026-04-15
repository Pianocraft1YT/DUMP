/*
 * Activity 4.1.3
 */
import java.io.File;
import java.io.IOException;
import java.util.Scanner;
import java.util.ArrayList;

public class GDPData
{
  private String country;
  private int yearFirst;
  private double gdpFirst;
  private int yearLast;
  private double gdpLast;
  
   /**
  * A class method to create a dataset of GDPData objects.
  * 
  * @param name of the data file to use
  * 
  * @return An ArrayList of GDPData 
  */
  public static ArrayList<GDPData> createDataSet(String filename) throws IOException
  {
    ArrayList<GDPData> data = new ArrayList<GDPData>();
      
    Scanner sc = new Scanner(new File(filename));
    
    String titleRow[] =  sc.nextLine().split(",");

    String tokens[];
    int first = 0;
    int last = 0;
    double gdpF = 0.0;
    double gdpL = 0.0;
    while (sc.hasNext()) 
    {
      tokens = sc.nextLine().split(",");
      last = tokens.length - 1;
      
      // find first year data was collected
      first = 4;
      while (tokens[first].equals(""))
      {
        first++;
      }
      gdpF = Double.parseDouble(tokens[first]);
      

      if (!tokens[last].equals(""))
      {
        gdpL = Double.parseDouble(tokens[last]);
      }
      // construct and add to data set
      data.add(new GDPData(tokens[0], Integer.parseInt(titleRow[first]), gdpF, Integer.parseInt(titleRow[last]), gdpL));
    }
   
    sc.close();
    
    return data;
  }
  
  /**
   * The constructor for the GDP class.
   * 
   * @param country A String with the name of the country
   * @param yearFirst The first year GDP was reported
   * @param gdpFirst The GDP from the first year
   * @param lastFirst The last year GDP was reported
   * @param gdpLast The GDP from the last year
   */
  public GDPData(String country, int yearFirst, double gdpFirst, int yearLast, double gdpLast)
  {
    this.country = country;
    this.yearFirst = yearFirst;
    this.gdpFirst = Math.round(gdpFirst);
    this.yearLast = yearLast;
    this.gdpLast = Math.round(gdpLast);
  }
  
  /**
   * Gets the country name.
   * 
   * @return a String with the country name
   */
  public String getCountry() {
    return country;
  }
  
  /**
   * Gets the GDP from the first year of data.
   * 
   * @return a double value of the GDP   
   */
  public double getGdpFirst() {
    return gdpFirst;
  }
  
  /**
   * Gets the GDP from the last year of data.
   * 
   * @return a double value of the GDP   
   */
  public double getGdpLast() {
    return gdpLast;
  }
  
  
  /**
   * Get the String representation of this object
   * 
   * @return country name with first and last year's GDP 
   * 
   */
  public String toString() {
    return country + ": " + yearFirst + ":$" + gdpFirst +  " " + yearLast + ":$" + gdpLast;
  }
}