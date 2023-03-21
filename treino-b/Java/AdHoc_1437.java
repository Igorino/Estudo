import java.io.IOException;
import java.util.Scanner;

public class AdHoc_1437 { 
 
    public static void main(String[] args) throws IOException {
 
        Integer numeroDeComandos = -1;
        String direcaoFinal;

        Scanner scan = new  Scanner(System.in);
        numeroDeComandos = Integer.parseInt(scan.nextLine().trim());  
        while (numeroDeComandos != 0) {

            String comandos = scan.nextLine();
            direcaoFinal = devolvePonteiroDaDirecao(numeroDeComandos, comandos);
            System.out.println(direcaoFinal);
            numeroDeComandos = Integer.parseInt(scan.nextLine().trim());  

        }
        scan.close();
    }
 
    public static String devolvePonteiroDaDirecao(Integer numeroDeComandos, String comandos) {

        String[] listaDeDirecoes = {"N", "L", "S", "O"};
        Integer ponteiro = 0;
        char comandoAtual = ' ';
        char[] comandosChar = comandos.toCharArray();

        for (int i = 0; i < numeroDeComandos; i++) {
            comandoAtual = comandosChar[i];
            if (comandoAtual == 'E') {
                if (ponteiro == 0) {
                    ponteiro = comandosChar.length;
                } else {
                    ponteiro--;
                }
            } else if (comandoAtual == 'D'){
                if (ponteiro == 4) {
                    ponteiro = 0;
                } else {
                    ponteiro++;
                }
            }
        }


        return listaDeDirecoes[ponteiro];
    }
}