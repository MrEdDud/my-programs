package rectcalc;
import java.util.*;

public class RectCalc {
    public static void main(String[] args) {
    Double total_per;
    Double total_area;
    
    Scanner input = new Scanner(System.in);
    
    System.out.println("Enter your length in cm");
    Double length = input.nextDouble();
    
    System.out.println("Enter your width in cm");
    Double width = input.nextDouble();
    
    total_per = (width*2)+(length*2);
    total_area = width * length;
    
    System.out.println("Your perimeter is " + total_per + "cm");
    System.out.println("Your area is " + total_area + "cm squared");
    }
}
