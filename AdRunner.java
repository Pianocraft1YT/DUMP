public class AdRunner {
public static void main(String[] args)
  {
    TargetedAd AR = new TargetedAd();
    AR.prepareAdvertisements("socialMediaPosts_500.txt", "targetWordsCat.txt", "targetWordsDog.txt");
  }
}
