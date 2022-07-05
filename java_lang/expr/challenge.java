//package Learning.java_lang.expr;

public class challenge {

    public static void main(String[] args){

        //Declare some integer variables
        int number = (10 + 5) + (2 * 10);
        int number2;
        int number3;

        System.out.println("My first number is: " + number);

        number2 = 12;
        number3 = 6;
        System.out.println("My second number is: " + number2);
        System.out.println("My third number is: " + number3);

        int total = number + number2 + number3;

        System.out.println("The total if all added together is: " + total);

        //Add some blank lines
        System.out.println();
        System.out.println();

        number3 = number * 2;

        total = number + number2 + number3;
        System.out.println("The total if all added together is: " + total);

        //Add some blank lines
        System.out.println();
        System.out.println();

        int finalNum =  total - 1000;

        System.out.print("The final number is: " + finalNum);




    }
    
}
