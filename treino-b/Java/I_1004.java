import java.io.IOException;
import java.util.Scanner;

public class I_1004 {
	
	int multiplicaNumeros(int X, int Y){
		int resultado = X * Y;
		return resultado;
	}
	
    public static void main(String[] args) throws IOException {
    	I_1004 calculo = new I_1004();
    	Scanner sc = new Scanner(System.in);
    	int X = sc.nextInt();
    	int Y = sc.nextInt();
		sc.close();
    	System.out.println("PROD = " + calculo.multiplicaNumeros(X, Y));
 
    }
 
}