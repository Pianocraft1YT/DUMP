

/*
 * Activity 3.1.3
 */
public class Pet
{
  public static final int CAT = 1;
  public static final int DOG = 2;
  
  private String name;
  private int type;
  private String owner;
  private static int totaldestroyedItems;
  private int energy;
  private int happy;
  private int health;
  private boolean alive;
  /*---------- constructors ----------*/
  public Pet(String name, int type)
  {
    this.name = name;
    this.type = type;
    health = 10;
    energy = 25;
    happy = 20;
    alive = true;
  }
  
  /*---------- accessors ----------*/
  public String getName()
  {
    return name;
  }
  
  public int getType()
  {
    return type;
  }
  
  public String getOwner()
  {
    return owner;
  }
  
  public String toString()
  {
    if (alive){
      String state = name + ", " + owner + "'s ";
    if (type == CAT)
      state += "cat: ";
    else if (type == DOG)
      state += "dog: ";
    state += "Happiness is " + happy + " and energy is " + energy;
    return state;
    }
    else{
      String state = (name + " is dead.");
      return state;
    }
    
  }
  
  /*---------- mutators ----------*/
  public void setName(String name)
  {
    this.name = name;
  }
  
  public void setOwner(String owner)
  {
    this.owner = owner;
  }
  /*---------- value changing methods: mutators ----------*/
  /*----------    that change happy or energy   ----------*/
  public void feed()
  {
    if (alive){
      energy += 10;
    happy += 5;
    System.out.println(name + " says: Mealtime!");
    }
    else
      System.err.println(name + " is dead.");
    
  }

  public void makeNoise()
  {
    if (alive){
      energy--;
    happy -= 5;
    if (type == CAT)
      System.out.println(name + " says: Meow!");
    else
      System.out.println(name + " says: Arf arf!");
  }
  else
    System.out.println(name + " is dead.");
  }
  public void walk()
  {
    if (type == DOG) 
    {
      happy += 10;
      energy -= 15;
      System.out.println(name + " says: Hooray! A walk!");
    }
    }
    
  
  
  public void giveTreat()
  {
    energy += 3;
    happy += 5;
    System.out.println(name + " says: Yum, a treat!");
  }

  public void groom()
  {
    energy -= 2;
    if (type == CAT)
    {
      happy += 5;
      System.out.println(name + " says: Purrrrrrrrrrrr!");
    }
    else if (type == DOG)
    {
      happy -= 2;
    }
  }
  
  public void play()
  {
    energy -= 5;
    happy += 5;
    System.out.println(name + " says: Oh boy! I get to play!");
  }

  public void sleep()
  {
    energy += 5;
    System.out.println(name + " says: zzzzzzzzzzzzzzzzzzz");

  }
  public void destroy()
  {
    int rand = (int) (Math.random()*(6)+1);
    totaldestroyedItems += rand;
    System.out.println(name + " broke " + rand + " items");
    System.out.println("Total items destroyed: " + totaldestroyedItems);
  }
  public void fight(Pet p)
  {
    if (this.alive && p.alive){
      int rand = (int) (Math.random()*10+1);
    if (rand < 5){
      rand = (int) (Math.random()*6+1);
      p.health -= rand;
    }
    else{
        rand = (int) (Math.random()*6+1);
        this.health -=rand;
    }
    if (this.health <= 0){
       this.alive = false;
      System.out.println(this.name + " died.");
    }
    else
      System.out.println(this.name + " fought " + p.name + ", and has " + this.health + " health left.");

    if (p.health <= 0)
    {
      p.alive = false;
      System.out.println(p.name + " died.");
    }
    else
      System.out.println(p.name + " has " + p.health + " health left.");
  }
  else{
      System.out.println("One or both pets are dead and cannot fight.");
    }
    }
    
    
  
}
