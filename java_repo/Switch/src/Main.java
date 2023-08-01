public class Main {
    public static void main(String[] args) {

        switch (1) {
            case 1 -> System.out.println("Value was 1");
            case 2 -> System.out.println("Value was 2");
            default -> System.out.println("Was not 1 or 2");
        }

        /*

         The above as an if statement

        int value = 1;

        if (value == 1){
            System.out.println("Value was 1");
        }else if (value == 2){
            System.out.println("Value was 2");
        } else{
            System.out.println("Was not 1 or 2");
        }

         */

        String month = "MARCH";
        System.out.println(month + " is in the " + getQuarter(month) + " quarter");
    }

    @org.jetbrains.annotations.Contract(pure = true)
    public static String getQuarter(String month){

        return switch (month){
            case "JANUARY", "FEBRUARY", "MARCH" -> "1st";
            case "APRIL", "MAY", "JUNE" -> "2nd";
            case "JULY", "AUGUST", "SEPTEMBER" -> "3rd";
            case "OCTOBER", "NOVEMBER", "DECEMBER" -> "4th";
            default -> "bad";
        };
    }
}
