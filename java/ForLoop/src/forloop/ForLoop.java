package forloop;
import java.util.*;

public class ForLoop {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.println("Enter your number");
        int userNum = input.nextInt();
        
        for (int i = 1; i <= userNum; ++i){
            System.out.println("*".repeat(i));
        } for (; userNum > 0; --userNum){
                System.out.println("*".repeat(userNum-1));
        }
    }
}
