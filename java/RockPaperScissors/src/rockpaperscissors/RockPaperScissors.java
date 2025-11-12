package rockpaperscissors;
import java.util.*;

public class RockPaperScissors {
    public static void main(String[] args) {
    
    Scanner input = new Scanner(System.in);
    
    System.out.println("Rock (0), Paper (1), Scissors (2)?");
    Double user_choice = input.nextDouble();
    
    Double random_num = Math.random();
    
    if (random_num > 0.66 && user_choice == 1) {
        System.out.println("Rock!");
        System.out.println("Player wins");
    }
    else if (random_num > 0.66 && user_choice == 2){
        System.out.println("Rock!");
        System.out.println("Computer wins");
    }
    else if (random_num > 0.33 && user_choice == 0){
        System.out.println("Paper!");
        System.out.println("Computer wins");
    }
    else if (random_num > 0.33 && user_choice == 2){
        System.out.println("Paper!");
        System.out.println("Player wins");
    }
    else if (random_num < 0.33 && user_choice == 0){
        System.out.println("Scissors!");
        System.out.println("Player wins");
    }
    else if (random_num < 0.33 && user_choice == 1){
        System.out.println("Scissors!");
        System.out.println("Computer wins");
    }
    else {
        System.out.println("Draw");    
    }
    } 
}
