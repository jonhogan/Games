import java.util.Scanner;
public class Main {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String isConvertible;

        Car car = new Car();

        System.out.println("Enter the color of the car.");
        car.setColor(scanner.nextLine());
        System.out.println("Enter the make of the car.");
        car.setMake(scanner.nextLine());
        System.out.println("Enter the model of the car.");
        car.setModel(scanner.nextLine());
        System.out.println("Enter the number of doors");
        car.setNumberOfDoors(Integer.parseInt(scanner.nextLine()));
        System.out.println("Is the car a convertible? (Yes/No)");
        isConvertible = scanner.nextLine().toLowerCase();
        car.setConvertible(isConvertible.equals("yes"));

        car.printCar();
    }
}
