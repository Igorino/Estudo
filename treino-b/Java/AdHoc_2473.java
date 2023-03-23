import java.io.IOException;
import java.util.Scanner;

public class AdHoc_2473 {
 
    public class Numeros {
        public int[] numerosJogados = new int[6];
        public int[] numerosSorteados = new int[6];

        public Numeros() {
            Scanner scan = new Scanner(System.in);
            for (int i = 0; i < 6; i++) {
                numerosJogados[i] = scan.nextInt();
            }   
            for (int i = 0; i < 6; i++) {
                numerosSorteados[i] = scan.nextInt();
            } 
            scan.close();
        }
    }
    public static void main(String[] args) throws IOException {
        int quantidadeDeAcertos = 0;

        AdHoc_2473 outer = new AdHoc_2473();
        Numeros numeros = outer.new Numeros();

        for (int i = 0; i < 6; i++) {
            if (temNoArray(numeros.numerosSorteados, numeros.numerosJogados[i]))
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