package timesthreenums;
import java.util.*;

public class TimesThreeNums {
    public static void main(String[] args) {
    Double total;
    
    Scanner input = new Scanner(System.in);
    
    System.out.println("Enter your first number");
    Double first_num = input.nextDouble();
    
    System.out.println("Enter your second number");
    Double second_num = input.nextDouble();
    
    System.out.println("Enter your third number");
    Double third_num = input.nextDouble();
    
    total = first_num * second_num * third_num;
    
    System.out.println("Your total is " + total);
    } 
}
