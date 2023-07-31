public class Main {
    public static void main(String[] args) {

        int feet = 8, inches = 11;
        double inCent;

        inCent = convertToCentimeter(inches);
        System.out.println(inches + " inches equals " + inCent + " centimeters.");

        inCent = convertToCentimeter(feet, inches);
        System.out.println(feet + " feet and " + inches + " inches equals " + inCent +
                           " centimeters.");

    }

    public static double convertToCentimeter(int inches){
        return (inches * 2.54);
    }

    public static double convertToCentimeter(int feet, int inches){
        int totalInches = (feet * 12) + inches;
        return (totalInches * 2.54);
    }
}
