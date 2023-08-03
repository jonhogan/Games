public class Main {
    public static void main(String[] args) {

        /*

        for(int i = 0; i < 5; i++) {
            System.out.println(i + 1);
        }



        for (double rate = 1; rate < 6; rate++) {

            System.out.println("Interest on $10,000 at " + rate +"% interest is: " +
                                calculateInterest(10_000.0, rate));
        }

         */

        for(double rate = 7.5; rate <= 10; rate += .25){

            System.out.println("Interest on $100.00 at " + rate +"% interest is: " +
                                calculateInterest(100.0, rate));
            if (rate == 8.5){
                break;
            }
        }
    }

    public static double calculateInterest(double amount, double interestRate){

        return (amount * (interestRate / 100));
    }

}
