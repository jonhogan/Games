public class Main {

    public static void main(String[] args) {
        int sumThis = 1000;

        System.out.println("The sum on of the numbers in " + sumThis + " is: " +
                sumDigits(sumThis));

    }

    public static int sumDigits(int x){

        int sum = 0;
        if(x < 0){
            sum = -1;
        }

        //get the right most digit, then truncate it
        while (x > 0){
            sum += (x % 10);
            x = x / 10;

        }

        return sum;
    }
}
