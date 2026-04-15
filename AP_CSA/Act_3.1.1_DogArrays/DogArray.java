/*
 * Activity 3.1.1
 */
public class DogArray
{
  public static void main(String[] args)
  {
    Dog[] myDogs = {new Dog("Number"), new Dog("HAHA"), new Dog("skull")};
    Dog[] neighborsDogs = new Dog[2];
    System.out.println(myDogs[0].getName());
    System.out.println(myDogs[1].getName());
    System.out.println(myDogs[2].getName());
    neighborsDogs[0] = new Dog("rizz");
    neighborsDogs[1] = new Dog("no rizz");
    System.out.println(neighborsDogs[0].getName());
    System.out.println(neighborsDogs[1].getName());
    // CODE TO ADD
    Dog[] friendsDogs = {new Dog("Lady"), new Dog("Tramp")};
    System.out.println(friendsDogs[0] + " and " + friendsDogs[1]);
//neighborsDogs = {new Dog("Cinnamon"), new Dog("Mocha")}; // error
//that errors because the jvm doesnt know what type it is, nor is it declared as an array.
//neighborsDogs[2] = new Dog("Cocoa"); // error
//error because you went out of bounds, its supposed to be [1]
//neighborsDogs = new Dog[3];
//System.out.println(neighborsDogs[0].getName()); // error
//System.out.println(neighborsDogs[1].getName()); // error
//every object in that is now null cant do anything with it so error
myDogs[2] = null; // gave my puppy to my neighbor!

  }
}