//package learning.java_lang.kilo;
import java.util.*;

/*
 * Short program to convert pounds to kilos
 * @version 1.0 07/05/2022
 * @author Jon Hogan
 * 
 */

public class kilo {

    public static void main(String[] arg){
        Scanner input = new Scanner(System.in);
        double kilo = 0.45359237;
        double pounds;
        double poundsToKilos;

        System.out.print("Enter the weight in pounds you would like to convert: ");

        pounds = Double.parseDouble(input.nextLine());
        poundsToKilos = pounds * kilo;

        System.out.println();
        System.out.println("The weight in kilograms is: " + poundsToKilos);

    }

    
}
