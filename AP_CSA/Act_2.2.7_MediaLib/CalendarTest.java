
    import java.util.Calendar;
public class CalendarTest{
    private static String lastModified;
    private static int amountChanges;
    Calendar calendar = Calendar.getInstance();
public CalendarTest(){
    int hour = calendar.get(Calendar.HOUR_OF_DAY); // 24-hour format
    int minute = calendar.get(Calendar.MINUTE);
    int second = calendar.get(Calendar.SECOND);
    int day = calendar.get(Calendar.DAY_OF_MONTH);
    int month = calendar.get(Calendar.MONTH);
    lastModified = "Last modified on month "+ month + " of the year, day " + day + ", at " + hour + ":" + minute + ":" + second;
    amountChanges++;
}
public void modify(){
    int hour = calendar.get(Calendar.HOUR_OF_DAY); // 24-hour format
    int minute = calendar.get(Calendar.MINUTE);
    int second = calendar.get(Calendar.SECOND);
    int day = calendar.get(Calendar.DAY_OF_MONTH);
    int month = calendar.get(Calendar.MONTH);
    lastModified = "Last modified on month "+ month + " of the year, day " + day + ", at " + hour + ":" + minute + ":" + second;
    amountChanges++;
}
public String getModified(){
    return lastModified;
}
public int getAmountChanges(){
    return amountChanges;
}
public String getTime(){
    Calendar cal = Calendar.getInstance();
    String dateTimeStr = cal.getTime().toString();
    return dateTimeStr;
}
}