/* 
 * Activity 4.1.2
 */
import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class HorseData
{
    public static void main(String[] args) throws IOException
    {
        Scanner sc = new Scanner(new File("horsedata.txt"));
        String name = null;
        Integer weight = null;
        Double age = null;
        Boolean newOrNot = false;
        int sumWeight = 0;
        double sumAge = 0;
        int numHorses = 0;
        double totalHay = 0;
        while (sc.hasNext()){
            name = sc.next();
            weight = sc.nextInt();
            age = sc.nextDouble();
            newOrNot = sc.nextBoolean();
            sumWeight += weight;
            sumAge += age;
            numHorses++;
            totalHay += (weight*0.025);
            System.out.println("Horse: " + name + ", weighs " + weight + " pounds, and is " + age + " years old.");
            if (newOrNot == false)
                System.out.println(name + " has been here awhile.");
            else
                System.out.println(name + " hasn't been here long.");
            
        }
        System.out.println("Average Weight of Horses: " + (sumWeight/numHorses*1.0));
        System.out.println("Average Age of Horses: " + (sumAge*1.0/numHorses*1.0));
        System.out.println("Hay Needed: " + totalHay);
    }
}