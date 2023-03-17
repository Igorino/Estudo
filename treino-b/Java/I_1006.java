import java.io.IOException;
import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.util.Scanner;


public class Main {
	
	double calculaMedia (double X, double Y, double Z){
		double resultado = (((X * 2) + (Y * 3) + (Z * 5)) / 10);
		return resultado;
	}
	
    public static void main(String[] args) throws IOException {
    	NumberFormat nf = new DecimalFormat("#0.0");
    	Main calculo = new Main();
    	@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);
    	double X = sc.nextDouble();
    	double Y = sc.nextDouble();
    	double Z = sc.nextDouble(); 
    	System.out.println("MEDIA = " + nf.format(calculo.calculaMedia(X, Y, Z)));
 
    }
 
}