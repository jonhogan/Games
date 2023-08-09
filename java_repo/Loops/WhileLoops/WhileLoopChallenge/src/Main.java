public class Main {
    public static void main(String[] args) {
        int number = 4;
        int finishNumber = 20;
        int counter = 0;
        int totalNumbers = 0;

        while (number <= finishNumber){
            number++;
            if(!isEven(number)){
                totalNumbers++;
                continue;
            }
            if(counter == 5){
                break;
            }
            System.out.println("Even Number: " + number);
            totalNumbers++;
            counter++;
        }

        System.out.println("A total of " + counter +
                " even numbers were found.");
        System.out.println("A total of " + totalNumbers +
                " numbers were processed.");
    }

    public static boolean isEven(int x){
        return (x % 2 == 0);
    }
}
