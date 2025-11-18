/*
 * Activity 2.1.4
 */
public class LetterFrequencies
{
	public static void main(String[] args)
	{
		String letters = "abcdefghijklmnopqrstuvwxyz"; 
		String phrase = "This is a phrase!";

		System.out.println("Letter frequencies in '" + phrase + "'");

    /* your code here */
	int start = 0;
	int end = phrase.length()-1;
	int count = 0;
for (check = letters.substring(start, start+1);phrase.equals(check); start++)
	while (start < end){
		for (phrase.substring(start, start+1);phrase.equals("e"); start++){
			count++;
		}
		end--;
	}
}
}
