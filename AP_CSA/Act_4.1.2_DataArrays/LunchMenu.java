/*
 * Activity 4.1.2
 */
import java.io.File;
import java.io.IOException;
import java.util.Scanner;
public class LunchMenu
{
    public static void main(String[] args) throws IOException
    {
        String output = null;
        String output2 = null;
        output="Served twice a month: ";
        output2="Served thrice a month: ";
        Scanner sc = new Scanner(new File("lunches.txt"));
        while(sc.hasNext()){
            String[] str = sc.nextLine().split(":");
            if (str[1].contains("2")){
                output+="\n"+str[0];
            }
            else
                output2+="\n"+str[0];
        }
        System.out.println(output + output2);
    }
}