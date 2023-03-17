import java.io.IOException;
import java.util.Scanner;

public class AdHoc_2342 {

    public static void main(String[] args) throws IOException {
        Integer resultado = -1;

        Scanner scan = new Scanner(System.in);
        int max = Integer.parseInt(scan.nextLine());
        String conta = scan.nextLine();
        String[] contaSplit = conta.split(" ");
        Integer x = Integer.parseInt(contaSplit[0]);
        String sinal = contaSplit[1];
        Integer y = Integer.parseInt(contaSplit[2]);
        scan.close();

        if (sinal.equals("*")) {
            resultado = (x*y);
        } else if (sinal.equals("+")) {
            resultado =  (x+y);
        }

        if (resultado > max) {
            System.out.println("OVERFLOW");
        } else {
            System.out.println("OK");
        }
    }
 
}