public class Main {
    public static void main(String[] args) {

        int newScore = calculateScore("Jon", 1337);

        System.out.println("New score is " + newScore + " points");

        newScore = calculateScore(241);

        System.out.println("New score is " + newScore + " points");

    }

    public static int calculateScore(String playerName, int score){

        System.out.println("Player " + playerName + " scored " + score + " points");
        return score *1_000;
    }

    public static int calculateScore(int score){

        System.out.println("Player scored " + score + " points");
        return score *1_000;
    }
}
