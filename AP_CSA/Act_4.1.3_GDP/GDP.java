/*
 * Activity 4.1.3
 *
 * Data attribute:
 * The World Bank:GDP (current US$): OECD National Accounts data files, CC BY 4.0
 */
import java.io.IOException;
import java.util.ArrayList;
public class GDP
{
    public static void main(String[] args) throws IOException
    {

        ArrayList<GDPData> ohio = GDPData.createDataSet("gdp_per_capita.csv");
        for (GDPData monkey: ohio){
            System.out.println(monkey);
        }
        System.out.println("Index of US: " + GDPSearch.find(ohio, 0, ohio.size(), "United States"));
        double max = 0.0;
        String country = null;
        for (int i = 0; i < ohio.size(); i++){
            if (ohio.get(i).getGdpLast() > max){
                max = ohio.get(i).getGdpLast();
                country = ohio.get(i).getCountry();
            }
            
        }
        System.out.println("Max GDP per Capita: " + country + " " + max);
        double low = 0.0;
        for (int i = 0; i < ohio.size(); i++){
            if (ohio.get(i).getGdpLast() - ohio.get(i).getGdpFirst() > low){
                                low = ohio.get(i).getGdpLast() - ohio.get(i).getGdpFirst();
                                country = ohio.get(i).getCountry();

            }
            
        }
        
        System.out.println("Biggest increase: " + country + " " + low);
        System.out.println(GDPSearch.findAbove(ohio, "United States"));
    }
}