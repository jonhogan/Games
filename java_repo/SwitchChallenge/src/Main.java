public class Main {
    public static void main(String[] args) {

        System.out.println(natoAlpha('a'));

    }

    public static String natoAlpha(char letter){
        switch (letter){
            case 'A': case 'a':
                return "Able";
            case 'B': case 'b':
                return "Baker";
            case 'C': case 'c':
                return "Charlie";
            case 'D': case 'd':
                return "Dog";
            case 'E': case 'e':
                return "Easy";
            default:
                return (letter + " not found");

        }
    }
}
