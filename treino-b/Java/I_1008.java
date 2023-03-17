import java.io.IOException;
import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.util.Scanner;


public class I_1008 {
	
	double calculaSalario (int horasTrabalhadas, double dinheiroPorHora){
		double resultado = (horasTrabalhadas * dinheiroPorHora);
		return resultado;
	}
	
    public static void main(String[] args) throws IOException {
    	NumberFormat nf = new DecimalFormat("#0.00");
    	I_1008 calculo = new I_1008();
    	@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);
    	int numero = sc.nextInt();
    	int horasTrabalhadas = sc.nextInt();
    	double dinheiroPorHora = sc.nextDouble();
		sc.close();
    	System.out.println("NUMBER = " + numero);
    	System.out.println("SALARY = U$ " + nf.format(calculo.calculaSalario(horasTrabalhadas, dinheiroPorHora)));
 
    }
 
}