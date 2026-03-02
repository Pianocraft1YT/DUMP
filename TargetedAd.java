/*
 * Problem 2.3.1 Sell My Pet Food
 */
public class TargetedAd {

public TargetedAd(){
}
public void prepareAdvertisements(String postsFilename, String catTargetFile, String dogTargetFile){
    DataCollector dc = new DataCollector();
    DataCollector dc2 = new DataCollector();
    dc.setData(postsFilename, catTargetFile);
    dc2.setData(postsFilename, dogTargetFile);
    String currentCheck = dc.getNextPost().toLowerCase();
    String currentCheck2 = dc2.getNextPost().toLowerCase();
    String currentTarget;
    String currentTarget2;
    String dogUsernames = "";
    String catUsernames = "";

    String[] bannedWordsDogs = {
      "don't want",
      "dont want",
      "do not want",
      "do not like",
      "don't like",
      "dont like",
      "cat",
      "$%#!",
      "after hiking all day",
      "Loose bark",
      "such a dog",
      "What a dog",
      "lazy dog",
      "$%#!",
      "poor dogs",
      "stripped bark",
      "small barking puppy",
      "cats",
      "Movement",
      "Barking like a dog",
      "$%!@",
      "Fresh bark",
      "after the storm",
    };
    while (!currentCheck2.equals("none")) { 
      currentTarget2 = dc2.getNextTargetWord().toLowerCase();
      while (!currentTarget2.equals("none")){
        boolean hasNegationDogs = false;
        for (String bad : bannedWordsDogs) {
          if (currentCheck.indexOf(bad) != -1) {
            hasNegationDogs = true;
          }
        if (currentCheck2.indexOf(currentTarget2) != -1 && !hasNegationDogs){
          int end = currentCheck2.indexOf(" ");
          String username = currentCheck2.substring(0, end);
          if (dogUsernames.indexOf(username) == -1){
            dogUsernames += username + " ";
          }
        }
        currentTarget2 = dc2.getNextTargetWord().toLowerCase();
      }      
      currentCheck2 = dc2.getNextPost().toLowerCase();
    }







    String[] bannedWordsCats = {
        "don't want",
        "dont want",
        "do not want",
        "motor",
        "engine",
        "don't like",
        "I swear",
        "Light",
        "dog",
        "are you a",
        "do you like",
        "catch my attention",
        "darn cat",
        "knocking pens down",
        "some sleep",
        "toppling things over",
        "after the storm",
    };
    while (!currentCheck.equals("none")){ 
      currentTarget = dc.getNextTargetWord().toLowerCase();
      while (!currentTarget.equals("none")){
        boolean hasNegationCats = false;
        for (String bad : bannedWordsCats) {
          if (currentCheck.indexOf(bad) != -1) {
            hasNegationCats = true;
          }
        }
          if (currentCheck.indexOf(currentTarget) != -1 && !hasNegationCats){
            int end = currentCheck.indexOf(" ");
            String username = currentCheck.substring(0, end);
            if (catUsernames.indexOf(username) == -1){
              catUsernames += username + " ";         
            }
          } 
        currentTarget = dc.getNextTargetWord().toLowerCase();
      }    
      currentCheck = dc.getNextPost().toLowerCase();  
    }

    dc.prepareAdvertisement("catAds.txt", catUsernames, "Your furry friend will love our cat food!");
    dc2.prepareAdvertisement("dogAds.txt", dogUsernames, "Your furry friend will love our dog food!");
  }

}
}
    /*  
     * TODO:
     * PREPARATION WORK
     * (1) Create a file called targetWords.txt. Populate this file with words on each line that
     *     you think would determine if a user is a dog or cat owner.
     * 
     * PROGRAMMING
     * (2) Create a new DataCollector object and set the data to "socialMediaPostsSmall.txt" and "targetWords.txt"
     *     Important: Use the socialMedialPostsSmall to create your algorithm. Using a small file will help you 
     *     generate your solution quicker and give you the ability to double check your work.
     * (3) Create a String variable to hold the names of all the user. (The first word of every post is 
     *     a person's username)
     * (4) Compare each user's post to each target word. If a user mentions a target word, add their username to 
     *     the String of users. Separate usernames with a space. 
     *         Hint: You can use loops to look through each word. 
     *         Hint2: You can use indexOf to check if a word is in a user post. 
     * 
     *    make every post and target word lowercase
     *    while post is avaliable[
     *        while target words is avaliable [
     *            if post indexOf targetWords is not equal to -1 [
     *                 seperate word by using index of " " in post
     *                 username = post.substring(0, end)
     *                  allUsernames += username
     *    ]
     *  ]
     * ]
     * (5) Once you have all the users, use your DataCollector's prepareAdvertisement method to prepare a file 
     *     with all users and the advertisement you will send them.
     *         Additional Info: The prepareAdvertisement creates a new file on your computer. Check the posts of
     *         some of the usernames to make sure your algorithm worked.
     * 
     * THE FINAL SOLUTION
     * (6) Your solution should work with the socialMedialPostsSmall.txt. Modify your DataCollector initialization
     *    so you use the socialMediaPosts.txt. You should now have a larger file of users to target.
     *
     *  ENHANCEMENTS for cat and dog specifications.
     *
     *
     *       for (String dog : dogWords)
     *      if (currentTarget.equals(dog)){
     *       catordog = "dog";
     *       break;
     *  }
     * for (String cat : catWords)
     *  if (currentTarget.equals(cat)){
     *   catordog = "cat"
     *  break;
     *   }
     *
     *   ensuring NO DUPLICATE usernames
     *   String usedUsernames;
     *  EXTRACT username
     *      IF usedUsernames does NOT contain username
     *             WRITE username to file
     *             ADD username to usedUsernames
     *      END IF
     *
     */


    




