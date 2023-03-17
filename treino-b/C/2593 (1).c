#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#define MAX 15000

// KMP

typedef struct ind{
	int numeroIndice;
	struct ind *proxIndice;
}Indices;

typedef struct node{
	char letra;
	Indices *indices;
	struct node *proxIrmao;
	struct node *primeiroFilho;
} No;

No *criaTrie(){
	No* trie;
	trie = (No*) malloc(sizeof(No));
	trie->proxIrmao = NULL;
	trie->primeiroFilho = NULL;
	return trie;
}

No *procuraEntreFilhos(No* noPai, char letra){
	No *aux = noPai->primeiroFilho;					
	
	if (aux == NULL) return NULL;					//					  	  TRIE
													//                 a----------------b
	if (aux->letra = letra){						//                 m            e-------a
		return aux;									//             o---a---e       l-s    l---i 
	} else if (aux->proxIrmao != NULL){				//             r  r-d          a t   d-a  l 
		while (aux != NULL){						//                g o            a   e    e
			if (aux->letra = letra) return aux;		//                o r         
			aux = aux->proxIrmao; 
		}
	} else {
		return NULL;
	}
}



void colocaIndice (No * noPai, int ind){
	Indices *aux = noPai->indices;
	if (aux == NULL){
		Indices* novoIndice = (Indices*) malloc(sizeof(Indices));
		noPai->indices = novoIndice;
		novoIndice->numeroIndice = ind;
		novoIndice->proxIndice = NULL;
	} else {
		while (aux->proxIndice != NULL){
			aux = aux->proxIndice;
		}
		Indices* novoIndice = (Indices*) malloc(sizeof(Indices));
		aux->proxIndice = novoIndice;
		novoIndice->numeroIndice = ind;
		novoIndice->proxIndice = NULL;
	}
}

void colocaIndiceNew (No * noPai, int ind){
	Indices *novoIndice = (Indices*) malloc(sizeof(Indices));
	Indices *aux = noPai->indices;
	if (aux == NULL){

	}
}


No *criaFilho(No* noPai, char letra){
	No *aux = noPai;
	No *novoNo;

	if (aux->primeiroFilho == NULL){ //Se nao tiver filho, poe no primero
		novoNo = (No*) malloc(sizeof(No));
		novoNo->proxIrmao = NULL;
		novoNo->letra = letra;
		novoNo->indices = NULL;
		aux->primeiroFilho = novoNo;
	} else { //Se tiver,  anda pelos irmaos do primeiro filho e cria o novo filho no final
		while (aux != NULL && aux->proxIrmao != NULL){
			aux = aux->proxIrmao;
		}
	
		novoNo = (No*) malloc(sizeof(No));
		novoNo->proxIrmao = NULL;
		novoNo->letra = letra;
		novoNo->indices = NULL;

		aux->proxIrmao = novoNo;
	}

	return novoNo;
}

No *montaTrie(No *trie, int numeroDePalavras, char texto[], char *palavras[], int tamanhoDoTexto){
	int indiceAtual = 0;
	int indiceDaPalavraAtual = 0;
	int i = 0;
	char c = texto[indiceDaPalavraAtual];
	//printf("%d\n", 2);
	No* novoNo = criaFilho(trie, c);
	novoNo->indices = NULL;
	/*/
	No *novoNo = (No*) malloc(sizeof(No));
	trie->primeiroFilho = novoNo;
	novoNo->letra = c;
	novoNo->proxIrmao = NULL;
	novoNo->indices = NULL;
	/*/
	
	No *aux = novoNo;
	No *temp;

	//c = texto[i];
	while (texto[indiceAtual] != '\0'){
		//printf("%d\n", indiceAtual);
		if (texto[indiceAtual] == ' '){
			//printf("-%d\n", indiceDaPalavraAtual);
			colocaIndice(aux, indiceDaPalavraAtual);
			aux = trie;
			indiceDaPalavraAtual = indiceAtual + 1;
			
		}
		c = texto[indiceDaPalavraAtual];
		temp = procuraEntreFilhos(aux, c);
		if (temp != NULL){
			aux = temp;
		} else {
			criaFilho(aux, texto[indiceDaPalavraAtual]);
		}
		indiceAtual++;
		//c = getc(stdin);		
	}
	return NULL;
}

// Checa pra ver se o char da posicao atual é um numero, se for, o texto acabou
bool textoTerminou (char x){ 
	if ((x == '1') ||
		(x == '2') ||
		(x == '3') ||
		(x == '4') ||
		(x == '5') ||
		(x == '6') ||
		(x == '7') ||
		(x == '8') ||
		(x == '9'))
	{
		return true;
	} else {
		return false;
	}
}

void criaTextoNew(char texto[], int *numeroDePalavras, int *tamanhoDoTexto){
	int i = 0;
	char x = getc(stdin);
	while (x != '\n'){
		texto[i] = x;
		i++;
		if (i = MAX) break;
		char x = getc(stdin);
	}
	*tamanhoDoTexto = i;
	scanf("%d", *numeroDePalavras);
	
}

void criaTextoOld(char texto[], int *numeroDePalavras, int *tamanhoDoTexto){
	int i = 0;
	while (i < MAX){
		char x = getc(stdin);
		if (textoTerminou(x) == true) {
			*numeroDePalavras = x - '0';  
			break;
		} else if (x != '\n'){
			texto[i] = x;
			i++;
			*tamanhoDoTexto = *tamanhoDoTexto + 1;
		}
	}
}

void zeraString(char texto[]){
	int i;
	int t = strlen(texto);
	for (i = 0; i < t; i++){
		texto[i] = ' ';
	}
}

void adicionaEspacos(char texto[], int tamanhoDoTexto){
	int tamanho = tamanhoDoTexto;
	char j, k;
	int a, b;
	//printf("-%s-\n", texto);

	while (tamanho - 1 >= 0){
		//printf("%c ", texto[tamanho]);
		texto[tamanho] = texto[tamanho - 1];
		tamanho--;
	}
	
	texto[0] = ' ';
	texto[tamanhoDoTexto + 1] = ' ';
	//printf("+%s+\n", texto);
	tamanhoDoTexto = tamanhoDoTexto + 2;
}

void criaTexto(char texto[], int *numeroDePalavras, int *tamanhoDoTexto){
	char textoTemp[MAX];
	//scanf("%[^\n]s", &textoTemp);
	//strcpy(texto, textoTemp);
	//int tamanhoTemp = strlen(textoTemp);
	//*tamanhoDoTexto = tamanhoTemp;
	scanf("%[^\n]s", &textoTemp);
	strcpy(texto, textoTemp);
	*tamanhoDoTexto = strlen(textoTemp);
	int numeroDePalavrasTemp;
	adicionaEspacos( texto, *tamanhoDoTexto);
	scanf("%d", &numeroDePalavrasTemp);
	*numeroDePalavras = numeroDePalavrasTemp;
}

int *computaFuncaoDePrefixo(char *palavra, int tamanho){
	int k = -1;
	int i = 1;
	int *pi = (int*) malloc(sizeof(int));
	//int *pi = malloc(sizeof(int) *tamanho);

	if (!pi)
		return NULL;
	pi[0] = k;

	for (i = 1; i < tamanho; i++){
		while (k > -1 && palavra[k + 1] != palavra[i])
			k = pi[k];
		if (palavra[i] == palavra[k + 1])
			k++;
		pi[i] = k;
	}
	return pi;
}

void imprimeIndices(No* noPai){
	Indices* aux = noPai->indices;

	printf("\n");
	while (aux != NULL){
		printf("%d", aux->numeroIndice);
		if (aux->proxIndice != NULL) printf(" ");
		aux = aux->proxIndice;
	}
}

void buscaImprimeTrie(No *trie, char palavra[]){
	char palavraParaProcurar[150];
	int i, tamanhoDaPalavra;
	tamanhoDaPalavra = strlen(palavra);
	tamanhoDaPalavra++;
	No *atual = trie;
	No *aux;
	No *ant;

	while (i < tamanhoDaPalavra){
		ant = atual;
		atual = procuraEntreFilhos(atual, palavra[i]);
		if (atual != NULL) i++;
	}
	
	imprimeIndices(ant);

}

void funcaoPrefixo(char *palavra, int M, int *temp){

    int len = 0;
 
    temp[0] = 0;

    int i = 1;
    while (i < M){
        if (palavra[i] == palavra[len]){
            len++;
            temp[i] = len;
            i++;
        } else {
            if (len != 0){
                len = temp[len-1];
 
                
                
            } else {
                temp[i] = 0;
                i++;
            }
        }
    }
}

void buscaEmKMP(char *palavraParaProcurar, char *texto){

    int M = strlen(palavraParaProcurar);
    int N = strlen(texto);
 
    int temp[M];
 
    funcaoPrefixo(palavraParaProcurar, M, temp);
 	
 	int hue = 0;
    int i = 0; 
    int j  = 0;
    while (i < N){
        if (palavraParaProcurar[j] == texto[i]){
            j++;
            i++;
        }
 
        if (j == M){
        	if (hue != 0){
        		printf(" ");
        	}
            printf("%d", i - j);
            j = temp[j - 1];
            hue++;
        }

        else if (i < N && palavraParaProcurar[j] != texto[i]){
            if (j != 0)
                j = temp[j - 1];
            else
                i = i + 1;
        }
    }
    if (hue == 0){
    	hue = -1;
    	printf("%d", -1);
    }
}

void buscaImprimeKMP (char *texto, int tamanhoDoTexto, char *palavraParaProcurar, int tamanhoDaPalavraPP, int numeroDePalavras){
	int i;
	int *pi = computaFuncaoDePrefixo(palavraParaProcurar, tamanhoDaPalavraPP);
	int k = -1;
	int hue = 1;
	int birl = -1;
	int palavrasEncontradas = 0;

	//if (!pi) printf("%d\n", birl);

	for (i = 0; i < tamanhoDoTexto + 1; i++){
		//printf("i: %d\n", i);
		///printf("k + 1: %d\n", k + 1);
		while (k > -1 && palavraParaProcurar[k + 1] != texto[i])
			k = pi[k];
		if (text