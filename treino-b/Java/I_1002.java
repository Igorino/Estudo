import java.io.IOException;
import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.util.Scanner;


public class I_1002 {
	
	double calculaArea (double X){
		double resultado = ((X * X) * 3.14159);
		return resultado;
	}
	
    public static void main(String[] args) throws IOException {
    	NumberFormat nf = new DecimalFormat("#0.0000");
    	I_1002 calculo = new I_1002();
    	Scanner sc = new Scanner(System.in);
    	double X = sc.nextDouble();
		sc.close();
    	System.out.println("A=" + nf.format(calculo.calculaArea(X)));
 
    }
 
}