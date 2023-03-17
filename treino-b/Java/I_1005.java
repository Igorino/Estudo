import java.io.IOException;
import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.util.Scanner;


public class Main {
	
	double calculaMedia (double X, double Y){
		double resultado = (((X * 3.5) + (Y * 7.5)) / 11);
		return resultado;
	}
	
    public static void main(String[] args) throws IOException {
    	NumberFormat nf = new DecimalFormat("#0.00000");
    	Main calculo = new Main();
    	@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);
    	double X = sc.nextDouble();
    	double Y = sc.nextDouble();
    	System.out.println("MEDIA = " + nf.format(calculo.calculaMedia(X, Y)));
 
    }
 
}