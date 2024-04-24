import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        // Set an arbitrary large number for min
        // and an arbitrary small number for max
        int maxNumber = Integer.MIN_VALUE;
        int minNumber = Integer.MAX_VALUE;

        String userInput;
        int userNumber;

        Scanner scanner = new Scanner(System.in);

        while (true){

            // Prompt user for a number
            System.out.println("Enter a whole number, enter anything else to quit:");
            userInput = scanner.nextLine();
            try{
                userNumber = Integer.parseInt(userInput);
                if(userNumber > maxNumber){
                    maxNumber = userNumber;
                }

                if(userNumber < minNumber){
                    minNumber = userNumber;
                }
                
            }catch (NumberFormatException n){
                break;
            }

            System.out.println("Max number is: " + maxNumber);
            System.out.println("Min number is: " + minNumber);
        }
    }
}
