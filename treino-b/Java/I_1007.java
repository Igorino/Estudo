import java.io.IOException;
import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.util.Scanner;


public class I_1007 {
	
	double calculaMedia (double A, double B, double C, double D){
		double resultado = ((A * B) - (C * D));
		return resultado;
	}
	
    public static void main(String[] args) throws IOException {
    	NumberFormat nf = new DecimalFormat("#0");
    	I_1007 calculo = new I_1007();
    	@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);
    	double A = sc.nextDouble();
    	double B = sc.nextDouble();
    	double C = sc.nextDouble(); 
    	double D = sc.nextDouble();
		sc.close();
    	System.out.println("DIFERENCA = " + nf.format(calculo.calculaMedia(A, B, C, D)));
 
    }
 
}