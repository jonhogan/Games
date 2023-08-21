public class Car {

    private String make;
    private String model;
    private String color;
    private int numberOfDoors;
    private boolean convertible;

   /* public void describeCar(){
        System.out.println("Doors: " + numberOfDoors + "-Door\n" +
                "Color: " + color + "\n" +
                "Make: " + make + "\n" +
                "Model: " + model + "\n" +
                "Top: " + (convertible ? "Convertible" : "Hard Top"));
    }*/

    public void setMake(String thisMake){
        make = thisMake;
    }

    public void setModel(String thisModel){
        model = thisModel;
    }

    public void setNumberOfDoors(int doors){
        numberOfDoors = doors;
    }

    public void setColor(String thisColor){
        color = thisColor;
    }

    public void setConvertible(boolean isConvertible){
        convertible = isConvertible;
    }

    public void printCar(){
        System.out.println("Car Description:\n" +
                            numberOfDoors + "-Door\n" +
                            "Color: " + color + "\n" +
                            "Make: " + make + "\n" +
                            "Model: " + model + "\n" +
                            "Style: " + (convertible ? "Convertible" : "Hard Top"));
    }

}
