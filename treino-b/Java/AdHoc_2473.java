import java.io.IOException;
import java.util.Scanner;

public class AdHoc_2473 {
 
    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(System.in);
        int quantidadeDeAcertos = 0;
        int[] numerosJogados = new int[6];
        int[] numerosSorteados = new int[6];;
        for (int i = 0; i < 6; i++) {
            numerosJogados[i] = scan.nextInt();
        }   
        for (int i = 0; i < 6; i++) {
            numerosSorteados[i] = scan.nextInt();
        }   
        scan.close();
        for (int i = 0; i < 6; i++) {
            if (temNoArray(numerosSorteados, numerosJogados[i]))
                quantidadeDeAcertos++;
        }   
        switch (quantidadeDeAcertos) {
            case 0:
            case 1:
            case 2:
                System.out.println("azar");
                break;
            case 3:
                System.out.println("terno");
                break;
            case 4:
                System.out.println("quadra");
                break;
            case 5:
                System.out.println("quina");
                break;
            case 6:
                System.out.println("sena");
                break; 
            default:
                break;
        }
        
    }
 
    public static boolean temNoArray(int[] array, int itemProcurado) {
        for (int i = 0; i < array.length; i++) {
            if (itemProcurado == array[i]) {
                return true;
            }
        }
        return false;
    }
}