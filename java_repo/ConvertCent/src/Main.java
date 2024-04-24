public class Main {
    public static void main(String[] args) {

        int feet = 5, inches = 68;
        double inCent;

        inCent = convertToCentimeter(inches);
        System.out.println(inches + " inches equals " + inCent + " centimeters.");

        inches = 8;

        inCent = convertToCentimeter(feet, inches);
        System.out.println(feet + " feet and " + inches + " inches equals " + inCent +
                           " centimeters.");

    }

    public static double convertToCentimeter(int inches){
        return (inches * 2.54);
    }

    public static double convertToCentimeter(int feet, int inches){
        int feetToInches = (feet * 12);
        double totalCentimeters = convertToCentimeter(feetToInches) +
                                  convertToCentimeter(inches);

        // This is redundant, I could have returned the above, without
        // assigning it to a variable
        return totalCentimeters;
    }
}
