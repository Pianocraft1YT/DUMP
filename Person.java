/*
 * Activity 4.1.4
 */
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.io.File;
import java.util.Scanner;

public class Person
{
  private String fname;
  private String lname;
  private int age;
  private String SSN;
  private String phone;
    
  public Person( String SSN){
    this.SSN = SSN;
  }
  
  public void add(String fname, String lname, int age, String phone) throws IOException
  {
    if (isNewEntry())
    {
      this.fname = fname;
      this.lname = lname;
      this.age = age;
      this.phone = phone;

      addToFile();
    }
    else
    {
      System.out.println("Error: An entry for this SSN already exists");
    }
  }
  
  private void addToFile() throws IOException
  {
    if ( (lname != null) && (fname != null) && (age >= 0) && (phone != null) )
    {
      /*
        BufferedWriter writes to a data file, one line at a time.
        It is outside the scope of the AP Exam.
      */
      BufferedWriter writer = new BufferedWriter(new FileWriter("employee.csv", true));
      writer.write(fname + "," + lname + "," + age + "," + phone + "," + SSN + "\n");
      writer.close();
      
      System.out.println(fname + " " + lname + " added.");
    }
    else {
      System.out.println("Missing data, entry not added.");
    }
  }
  

  private boolean isNewEntry()  throws IOException
  {
    Scanner sc = new Scanner(new File("employee.csv"));
    String tokens[];
    boolean isNew = true;
    while(sc.hasNext()) 
    {
      tokens = sc.nextLine().split(",");
      if (tokens[4].equals(this.SSN))
      {
        // entry with SSN already exists 
        isNew = false;
      }
    }
    return isNew;
  }
}