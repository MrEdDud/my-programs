import java.util.Scanner;

public class Calculator {

    // Variables
    private double firstNumber = 0;
    private double secondNumber = 0;

    // New method to get user input
    public void getInput() {
        Scanner scanner = new Scanner(System.in); // A class used to get inputs
        boolean validInput = false;
        // Gets the first input
        System.out.print("Enter your first number: "); // Displays message
       
        // Checking if input == num
        while (!validInput) {
            try {
                firstNumber = scanner.nextDouble(); // Gets input
                validInput = true;
            } catch (Exception e) {
                System.out.println("That's not a valid input! Please try again.");
                scanner.nextLine();
            }    
        }
        
        validInput = false;

        // Gets the second input
        System.out.print("Enter your second number: "); // Displays message

        // Checking if input == num 
        while (!validInput) {
            try {
                secondNumber = scanner.nextDouble(); // Gets input
                validInput = true;
            } catch (Exception e) {
                System.out.println("That's not a valid input! Please try again.");
                scanner.nextLine();
            }    
        }
    }

    // New method to calculate the total
    public void calculateTotal() {
        double total = firstNumber + secondNumber; // Calculates total
        System.out.print("The total is " + total); // Displays total
    }

    // Main method which runs the program
    public static void main(String[] args) {
        Calculator calculator = new Calculator();
        calculator.getInput();
        calculator.calculateTotal();
    }
}