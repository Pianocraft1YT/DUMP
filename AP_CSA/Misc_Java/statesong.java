public class statesong
{
    public static void main(String[] args)
    {
String songLineOne = "I love you, California, you’re the greatest state of all.\nI love you in the winter, summer, spring and in the fall.";
System.out.println(songLineOne);
//That was a string literal
String songLineTwo = "I love your fertile valleys; your dear mountains I adore.\n";
songLineTwo = songLineTwo.concat("I love your grand old ocean and I love her rugged shore.");
System.out.println(songLineTwo);
//All strings are immutable, and there is your concatenation
String songLineThree = "It is here nature gives of her rarest, it is Home Sweet Home to me,\n";
songLineThree += "And I know when I die I shall breathe my last sigh\n";
songLineThree = songLineThree + "For my sunny California.\n";
System.out.println(songLineThree);
//There is your += and + 
int SixSeven = 67;
String songLineFour = "The End. " + SixSeven;
System.out.println(songLineFour);
//And that is your implicit type conversion
    }
}
