public class Car {

    private String make;
    private String model;
    private String color;
    private int numberOfDoors;
    private boolean convertible;

    public void setMake(String make){
        this.make = make;
    }

    public void setModel(String model){
        this.model = model;
    }

    public void setNumberOfDoors(int numberOfDoors){
        this.numberOfDoors = numberOfDoors;
    }

    public void setColor(String color){
        this.color = color;
    }

    public void setConvertible(boolean convertible){
        this.convertible = convertible;
    }

    public void printCar(){
        System.out.println("Car Description:\n" +
                            numberOfDoors + "-Door\n" +
                            "Color: " + color + "\n" +
                            "Make: " + make + "\n" +
                            "Model: " + model + "\n" +
                            "Style: " + (convertible ? "Convertible" : "Hard Top"));
    }

    public String getMake() {
        return make;
    }

    public String getModel() {
        return model;
    }

    public String getColor() {
        return color;
    }

    public int getNumberOfDoors() {
        return numberOfDoors;
    }

    public boolean isConvertible() {
        return convertible;
    }
}
