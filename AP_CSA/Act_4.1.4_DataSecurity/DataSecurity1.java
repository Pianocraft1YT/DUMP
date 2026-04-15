/*
 * Activity 4.1.4
 */
import java.io.IOException;

public class DataSecurity1
{ 
  public static void main(String[] args) throws IOException
  { 
    Person p = new Person("123-456-7890");
    p.fname = "Jane";
    p.lname = "Doe";
    p.age = 30;
    p.phone = "800-555-0256";

    p.add();
    
  }
} 