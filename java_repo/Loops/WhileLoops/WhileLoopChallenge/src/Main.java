public class Main {
    public static void main(String[] args) {
        int number = 4;
        int finishNumber = 20;
        int counter = 0;

        while (number <= finishNumber){
            number++;
            if(!isEven(number)){
                continue;
            }
            if(counter == 5){
                break;
            }
            System.out.println("Even Number: " + number);
            counter++;
        }

        System.out.println("A total of " + counter +
                " even numbers were found.");
    }

    public static boolean isEven(int x){
        return (x % 2 == 0);
    }
}
