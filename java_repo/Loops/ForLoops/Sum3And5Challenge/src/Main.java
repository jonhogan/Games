public class Main {

    public static void main(String[] args) {
        int total = 0, count = 0;

        for (int i = 1; i < 1001; i++) {
            if((i % 3 == 0) && i % 5 == 0){
                total += i;
                System.out.println("Then number " + i +" can be divided by both 3 and 5.");
                count++;
            }
            if(count == 5){
                break;
            }
        }

        System.out.println("The sum of the first 5 " +
                "numbers that can be divided by 3 and 5 is: " + total);

    }
}
