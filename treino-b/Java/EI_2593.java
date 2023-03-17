import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
 
/**
 * IMPORTANT: 
 *      O nome da classe deve ser "Main" para que a sua solução execute
 *      Class name must be "Main" for your solution to execute
 *      El nombre de la clase debe ser "Main" para que su solución ejecutar
 */
public class EI_2593 {

    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        
        //System.out.println("Por favor, insira o texto: ");
        String texto = scanner.nextLine();
        texto = String.format(" %s ", texto); 
        
        //System.out.println("Por favor, digite o numero de palavras a serem procuradas: ");
        Integer quantidadeDePalavras = Integer.parseInt(scanner.nextLine());

        //System.out.println("Por favor, digite as palavras: ");
		String palavrasString = scanner.nextLine();
        String[] palavras = palavrasString.split(" ");

        printaPosicoesDasPalavras(texto, palavras, quantidadeDePalavras);
    }
 
    public static void achaEPrintaPosicoesDaPalavra(String texto, String palavraOld) {
        List<Integer> resultado = new ArrayList<>();
        String palavra =String.format(" %s ", palavraOld); 

        for (int i = 0; i < texto.length() - palavra.length(); i++) {
            for (int j = 0; j < palavra.length(); j++) {
                if (texto.charAt(i + j) != palavra.charAt(j)) 
                    break;

                if (j == palavra.length()-1) {
                    resultado.add(i);
                }
            }
        }

        if (resultado.isEmpty())
            resultado.add(-1);

        String resultadoString = resultado.toString().replaceAll("([,\\[\\]])", "");

        System.out.println(resultadoString);
    }
    
    public static void printaPosicoesDasPalavras(String texto, String[] palavras, Integer quantidadeDePalavras) {
        for (int i = 0; i < quantidadeDePalavras; i++) {
            achaEPrintaPosicoesDaPalavra(texto, palavras[i]);
        }
    }
}