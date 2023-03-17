import java.io.IOException;
import java.util.Scanner;

public class Main {
	
	int somaNumeros(int X, int Y){
		int resultado = X + Y;
		return resultado;
	}
	
    public static void main(String[] args) throws IOException {
    	Main soma = new Main();
    	Scanner sc = new Scanner(System.in);
    	int X = sc.nextInt();
    	int Y = sc.nextInt();
    	System.out.println("X = " + soma.somaNumeros(X, Y));
 
    }
 
}