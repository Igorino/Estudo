import java.io.IOException;
import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.util.Scanner;


public class Main {
	
	double calculaArea (double X){
		double resultado = ((X * X) * 3.14159);
		return resultado;
	}
	
    public static void main(String[] args) throws IOException {
    	NumberFormat nf = new DecimalFormat("#0.0000");
    	Main calculo = new Main();
    	Scanner sc = new Scanner(System.in);
    	double X = sc.nextDouble();
    	System.out.println("A=" + nf.format(calculo.calculaArea(X)));
 
    }
 
}