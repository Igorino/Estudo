import java.io.IOException;
import java.util.Scanner;
 
public class AdHoc_1743 {
 
    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(System.in);
        
        Integer[] parte1 = {0,0,0,0,0};
        Integer[] parte2 = {0,0,0,0,0};
        
        for (int i = 0; i < 5; i++) {
            parte1[i] = scan.nextInt();
        }
        for (int i = 0; i < 5; i++) {
            parte2[i] = scan.nextInt();
        }
        scan.close();

        for (int i = 0; i < 5; i++) {
            if (parte1[i] == parte2[i]) {
                System.out.println("N");
                return;
            }
        }
        System.out.println("Y");
    }
 
}