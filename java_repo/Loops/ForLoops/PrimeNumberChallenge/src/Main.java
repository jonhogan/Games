import com.sun.source.tree.WhileLoopTree;

public class Main {

    public static void main(String[] args){
        int counter = 0;

        for(int i = 0; i <= 100_000; i++){
            if(isPrime(i)) {
                System.out.println(i + " is a prime number");
                counter++;
            }
        }

        System.out.print("\nThere were " + counter + " prime numbers found.");

    }

    public static boolean isPrime(int wholeNumber){

        boolean primeNumber = true;

        if(wholeNumber <= 2) {
            primeNumber = (wholeNumber == 2);
        }else{
            for(int div = 2; div <= (wholeNumber / 2); div++){
                if(wholeNumber % div == 0){
                    primeNumber = false;
                    break;
                }
            }
        }

        return primeNumber;

    }
}
