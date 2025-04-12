import java.util.Scanner;

public class ChristmasGiftCalculator {
    // Variables
    private double giftAmount = 0;
    private double weight = 0;
    private double totalWeight = 0;

    // Getting the amount of gifts
    public double getGiftAmount() {
        Scanner scanner = new Scanner(System.in); // A class used to get inputs
        boolean validInput = false;
        
        System.out.print("How many gifts do you have? ");

        // Checking if input == num
        while (!validInput) {
            try {
                giftAmount = scanner.nextDouble(); // Gets input
                validInput = true;
            } catch (Exception e) {
                System.out.println("That's not a valid input! Please try again.");
                scanner.nextLine();
            }    
        }
        return giftAmount;
    }

    public void getWeight(double amount) {
        Scanner scanner = new Scanner(System.in);

        for (int x = 0; x < amount; x++) {
            System.out.print("Enter the weight of gift " + (x + 1) + ": ");
            boolean validInput = false;

            while (!validInput) {
                try {
                    weight = scanner.nextDouble(); // Gets input
                    validInput = true;
                } catch (Exception e) {
                    System.out.println("That's not a valid input! Please try again.");
                    scanner.nextLine();
                }    
            } // While loop end

            if ((totalWeight += weight) > 500) {
                System.out.print("You fat pig this weighs too much.");
                break;
            } else {
                System.out.print("Success \n");
            }

        }
        
        scanner.close(); // Closing the scanner to avoid resource leaks
    }
    public static void main(String[] args) {
        ChristmasGiftCalculator xmascalculator = new ChristmasGiftCalculator();
        // giftAmount in this case is a local variable due to it being in the main() method
        double giftAmount = xmascalculator.getGiftAmount();
        xmascalculator.getWeight(giftAmount);
    }
}