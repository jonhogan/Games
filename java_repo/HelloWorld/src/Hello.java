public class Hello {

    public static void main(String[] args) {
        System.out.println("Hello, Jon");

        boolean isAlien = false;
        if (!isAlien) {
            System.out.println("Is not an alien!");
            System.out.println("And I'm scare of aliens");
        }

        int topScore = 90;
        if (topScore >= 100){
            System.out.println("You got the high score!");
        }

        int secondTopScore = 95;
        if(topScore > secondTopScore && topScore < 100){
            System.out.println("Greater than second top score and less than 100");
        }

        if((topScore > 90) || (secondTopScore <= 90)){
            System.out.println("Either or both of the conditions are true");
        }

    }
}
