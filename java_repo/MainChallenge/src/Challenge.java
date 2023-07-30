public class Challenge {
    public static void main(String[] args) {

        boolean gameOver = true;
        int score = 800;
        int levelCompleted = 5;
        int bonus = 100;
        int finalScore = 0;

        if (gameOver){
            finalScore = calculateScore(score, levelCompleted, bonus);
            System.out.println("Your final score was " + finalScore);
        }

        score = 10_000;
        levelCompleted = 8;
        bonus = 200;
        finalScore = score;

        if (gameOver){
            finalScore = calculateScore(score, levelCompleted, bonus);
            System.out.println("Your final score was " + finalScore);
        }
    }

    public static int calculateScore(int thisScore, int thisLevelCompleted, int thisBonus){
        int calcScore = thisScore + (thisLevelCompleted * thisBonus) + 1_000;
        return (calcScore);

    }
}
