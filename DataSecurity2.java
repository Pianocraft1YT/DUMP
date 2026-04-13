/*
 * Activity 4.1.4
 */
import java.io.IOException;

public class DataSecurity2
{ 
  public static void main(String[] args) throws IOException
  { 
    Person p = new Person("123-456-7890");
    
    p.add(null, "Doe", 30, "800-555-0256");

  }
} 
