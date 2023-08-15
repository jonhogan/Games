import java.util.Scanner;

public class Main {

    public static void main(String[] args) {


        int currentYear = 2023;

        /*
        String yearOfBirth = "1983";

        int intYearOfBirth = Integer.parseInt(yearOfBirth);

        System.out.println("Your age is: " + (currentYear - intYearOfBirth));

         */
        try {
            System.out.println(getInputFromConsole(currentYear));
        }catch (NullPointerException e){
            System.out.println(getInputFromScanner(currentYear));
        }

    }

    public static String getInputFromConsole(int currentYear){

        String name = System.console().readLine("Hi, what's your name? ");
        System.out.println("Hi, " + name + ", it is nice to meet you.");
        String yearOfBirth = System.console().readLine("What year were you born? " );

        int age = currentYear - (Integer.parseInt(yearOfBirth));

        return "You are " + age + " years old.";
    }

    public static String getInputFromScanner (int currentYear){
        Scanner scanner = new Scanner(System.in);

        System.out.println("Hi, what is your name? ");
        String name = scanner.nextLine();

        System.out.println("Hello, " + name + ", it is nice to meet you.");

        int age = checkData(currentYear);
        return "You are " + age + " years old.";
    }

    public static int checkData(int currentYear){
        Scanner scanner = new Scanner(System.in);
        String birthYear = "";
        int yearOfBirth = 0;

        boolean validYear = false;

        while(!validYear){
            System.out.println("What year were you born? ");
            birthYear = scanner.nextLine();
            try {
                yearOfBirth = Integer.parseInt(birthYear);

            }catch(NumberFormatException n) {
                System.out.println("Please enter a valid numeric year.");
                continue;
            }

            if(yearOfBirth < 0){
                System.out.println("Year of birth must be a positive number.");
            }else if ((currentYear - yearOfBirth) > 124){
                System.out.println("It is highly unlikely you are 125 or greater years old,"+
                        " please re-enter your birth year");
            }else{
                validYear = true;
            }
        }

        return currentYear - yearOfBirth;

    }
}
