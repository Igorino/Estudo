import java.io.IOException;
import java.util.Scanner;

public class I_1003 {
	
	int somaNumeros(int X, int Y){
		int resultado = X + Y;
		return resultado;
	}
	
    public static void main(String[] args) throws IOException {
    	I_1003 soma = new I_1003();
    	Scanner sc = new Scanner(System.in);
    	int X = sc.nextInt();
    	int Y = sc.nextInt();
		sc.close();
    	System.out.println("SOMA = " + soma.somaNumeros(X, Y));
 
    }
 
}