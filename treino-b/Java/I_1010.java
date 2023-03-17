import java.io.IOException;
import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.util.Scanner;


public class I_1010 {
	
	double calculaPreco (int quantidadeDePecas, double precoUnitario, int quantidadeDePecas2, double precoUnitario2){
		double resultado = (quantidadeDePecas * precoUnitario) + (quantidadeDePecas2 * precoUnitario2);
		return resultado;
	}
	
    public static void main(String[] args) throws IOException {
    	NumberFormat nf = new DecimalFormat("#0.00");
    	I_1010 calculo = new I_1010();
    	@SuppressWarnings("resource")
		Scanner sc = new Scanner(System.in);
    	sc.nextInt();
    	int quantidadeDePecas = sc.nextInt();
    	double precoUnitario = sc.nextDouble();
    	sc.nextInt();
    	int quantidadeDePecas2 = sc.nextInt();
    	double precoUnitario2 = sc.nextDouble();
		sc.close();
    	System.out.println("VALOR A PAGAR: R$ " + nf.format(calculo.calculaPreco(quantidadeDePecas, precoUnitario, quantidadeDePecas2, precoUnitario2)));
 
    }
 
}