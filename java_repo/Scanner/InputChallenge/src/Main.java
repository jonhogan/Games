import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        int count = 0;
        int userNumber;
        int sum = 0;

       do{
            userNumber = getInput(count);
            if (userNumber == Integer.MIN_VALUE){
                continue;
            }
            sum += userNumber;
            count++;

        }while (count < 5);

       System.out.println("Your total is: " + sum);


    }

    public static int validateInteger(String userInput){
        int number;
        try {
            number = Integer.parseInt(userInput);
        }catch (NumberFormatException n){
            System.out.println("Please enter a valid number.");
            return Integer.MIN_VALUE;
        }

        return number;
    }

    public static int getInput(int count){
        Scanner scanner = new Scanner(System.in);
        int userNumber;

        // This will only be valid for numbers less than 20,
        // conditions could be extended to encompass higher numbers.
        // That would be outside the scope of this program, just something
        // to keep in mind.
        if(count == 0){
            System.out.println("Enter the 1st number.");
        }else if (count == 1){
            System.out.println("Enter the 2nd numbers.");
        }else if (count == 2){
            System.out.println("Enter the 3rd number.");
        }else{
            System.out.println("Enter the " + (count + 1) + "th number.");
        }

        userNumber = validateInteger(scanner.nextLine());

        scanner.close();
        return userNumber;
    }
}
