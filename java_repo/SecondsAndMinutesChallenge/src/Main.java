public class Main {
    public static void main(String[] args) {

        // Test case
        System.out.println(getDurationString(3945));
        System.out.println(getDurationString(0, 59));

    }

    public static String getDurationString(int seconds){
        int minutes = seconds/60;
        seconds = (seconds % 60);

        return getDurationString(minutes, seconds);
    }

    public static String getDurationString(int minutes, int seconds){
        String time;
        if ((minutes < 0) || (seconds < 0)){

            time = "Invalid time(s), please check that minutes and seconds are positive numbers";

        } else if (seconds > 59) {

            time = "Invalid time, your seconds should not exceed 59 seconds.";

        } else {

            int hours = minutes / 60;
            minutes = (minutes % 60);
            time =  (hours + "h " + minutes + "m " + seconds + "s");

        }

        return time;
    }
}
