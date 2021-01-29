
class Main {
    public static void main(String[] args) {
        System.out.println('Hola mundo');
        Car car = new Car("AMQ123", new Account("Andres J", "AMQ123"));
        car.passenger = 4;
        car.printDataCar();
    }
}