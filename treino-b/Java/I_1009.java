import java.io.IOException;
import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.util.Scanner;


public class I_1009 {
	
	double calculaSalario (double salarioFixo, double montanteDeVendas){
		double resultado = salarioFixo + (montanteDeVendas * 0.15);
		return resultado;
	}
	
    public static void main(String[] args) throws IOException {
    	NumberFormat nf = new DecimalFormat("#0.00");
    	I_1009 calculo = new I_1009();
		Scanner sc = new Scanner(System.in);
    	sc.nextLine();
    	double salarioFixo = sc.nextDouble();
    	double montanteDeVendas = sc.nextDouble();
		sc.close();
    	System.out.println("TOTAL = R$ " + nf.format(calculo.calculaSalario(salarioFixo, montanteDeVendas)));
 
    }
 
}