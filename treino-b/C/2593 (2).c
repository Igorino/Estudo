#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <string.h>

#define MAX 15000

// Estou usando Trie

typedef struct ind{
	int numeroIndice;
	struct ind *proxIndice;
}Indices;

/*/
typedef struct ind{
	int numeroIndice;
	char tabelaIndices[MAX];
}Indices;
/*/

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
	trie->letra = '0';
	return trie;
}

No *procuraEntreFilhosOld(No* noPai, char letra){
	No *aux = noPai->primeiroFilho;					
	

	if (noPai->primeiroFilho == NULL) return NULL;	//					  	  TRIE
													//                 a----------------b
	if (noPai->primeiroFilho->letra == letra){		//                 m            e-------a
		return noPai->primeiroFilho;				//             o---a---e       l-s    l---i 
	} else if (aux->proxIrmao != NULL){				//             r  r-d          a t   d-a  l 
		while (aux != NULL){						//                g o            a   e    e
			if (aux->letra == letra) return aux;	//                o r         
			aux = aux->proxIrmao; 
		}
	} else {										
		return NULL;								
	}												
}													
													
No *procuraEntreFilhos(No* noPai, char letra){
	
	//printf("\n+++Procurando [[%c]] em filhos de [%c]\n", letra, noPai->letra);
	
	if (noPai->primeiroFilho == NULL){
		//printf("[[%c]] NAO eh filho de [%c]\n", letra, noPai->letra);
		return NULL;
	}
	else if(noPai->primeiroFilho->letra == letra){
		//printf("[[%c]] eh primeiro filho de [%c]\n", letra, noPai->letra);
		return noPai->primeiroFilho;
	}
	else {
		No* aux = noPai->primeiroFilho;
		while (aux != NULL){
			//printf("(aux->letra = %c)\n", aux->letra);
			
			if(aux->letra == letra){
				return aux;
				//printf("[[%c]] eh filho de [%c]\n", letra, noPai->letra);
			}
			
			aux = aux->proxIrmao;
			
		}
	}
	//printf("[[%c]] NAO eh filho de [%c]\n", letra, noPai->letra);
	return NULL;
}

void imprimeTexto (int tamanhoDoTexto, char texto[]){
	int i = 0;
	printf("\n");
	for (i = 0; i < tamanhoDoTexto; i++){
		printf("%c", texto[i]);
	}
	printf("\n");
}
										
void colocaIndice (No * noPai, int ind){
	Indices *aux = noPai->indices;
	Indices* novoIndice = (Indices*) malloc(sizeof(Indices));
	novoIndice->proxIndice = NULL;
	novoIndice->numeroIndice = ind;

	if (noPai->indices == NULL){
		noPai->indices = novoIndice;
		
		
	} else {
		while (aux->proxIndice != NULL){
			aux = aux->proxIndice;
		}
		aux->proxIndice = novoIndice;
	}
	//printf("-Colocando Indice (%d) na letra [%c]\n", ind, noPai->letra);
}

No *criaFilho(No* noPai, char letra){
	No *aux = noPai->primeiroFilho;
	No *novoNo = (No*) malloc(sizeof(No));;
	novoNo->primeiroFilho = NULL;
	novoNo->proxIrmao = NULL;
	novoNo->letra = letra;
	novoNo->indices = NULL;
	//iniciaTabela(novoNo);

	if (noPai->primeiroFilho == NULL){ //Se nao tiver filho, poe no primero
		noPai->primeiroFilho = novoNo;

	} else { //Se tiver,  anda pelos irmaos do primeiro filho e cria o novo filho no final
		
		while (aux != NULL && aux->proxIrmao != NULL){
			aux = aux->proxIrmao;
		}
		aux->proxIrmao = novoNo;
	}

/*/
	if (noPai->letra != '0'){
		printf("\nPai: %c\n", noPai->letra);
	} else {
		printf("\nPai: RAIZ DA TRIE\n");
	}
	printf("Criando Filho [[%c]] em [%c]\n", novoNo->letra, noPai->letra);
/*/

	return novoNo;
}

No *montaTrie(No *trie, int numeroDePalavras, char texto[], char *palavras[], int tamanhoDoTexto){
	int indiceAtual = 0;
	int indiceDaPalavraAnterior = 0;
	int i = 0;
	char c = texto[indiceAtual];
	//printf("%d\n", 2);
	
	No* novoNo = criaFilho(trie, texto[indiceAtual]);
	novoNo->indices = NULL;
	
	texto[tamanhoDoTexto] = ' ';
	tamanhoDoTexto = tamanhoDoTexto + 1;

	No *aux = novoNo;
	//No *aux;
	No *temp;

	//imprimeTexto(tamanhoDoTexto, texto);

	//c = texto[i];
	while (texto[indiceAtual + 1] != '\0'){
		
		indiceAtual++;
		
		//printf("Indice atual: %d\n", indiceAtual);
		c = texto[indiceAtual];
		if (texto[indiceAtual] == ' '){
			////printf("-%d\n", indiceDaPalavraAnterior);
			colocaIndice(aux, indiceDaPalavraAnterior);
			////printf("indiceDaPalavraAnterior: %d\n", indiceDaPalavraAnterior);
			aux = trie;
			//printf("AUX  %d\n", aux);
			//printf("TRIE %d\n", trie);
			indiceDaPalavraAnterior = indiceAtual + 1;
			
		} else {
			//printf("\n[%c] nao eh espaco\n", texto[indiceAtual]);
			temp = procuraEntreFilhos(aux, texto[indiceAtual]);
			//printf("TEMP %d\n", temp);
			if (temp != NULL){
				aux = temp;
			} else if (temp == NULL){
				aux = criaFilho(aux, texto[indiceAtual]);
			}	
		}
		
		//indiceAtual++;
		
		//c = getc(stdin);		
	}
	return NULL;
}

void imprimeIndices(No* noPai){
	Indices* aux = noPai->indices;
	//printf("teste\n");
	if (aux == NULL){
		printf("-1");
		exit;
	}
	while (aux != NULL){
		//printf("Numero Indice de [%c]: %d\n", noPai->letra, aux->numeroIndice);
		printf("%d", aux->numeroIndice);
		if (aux->proxIndice != NULL) 
			printf(" ");
		aux = aux->proxIndice;
	}
	printf("\n");
}

void buscaImprimeTrie(No *trie, char palavra[]){
	char palavraParaProcurar[60];
	int i = 0;
	int tamanhoDaPalavra = strlen(palavra);
	No *atual = trie;
	No *aux;
	No *ant = atual;
	
	/*/
	printf("\n----------------------------------------------\n");

	printf("\nProcurando por: %s\n", palavra);
	printf("Tamanho da palavra: %d\n", tamanhoDaPalavra);
	/*/

	while (i < tamanhoDaPalavra){
		/*/
		printf("\n->i: %d\n", i);
		printf("Palavra[i]: %c\n", palavra[i]); //i = 2 tamanho = 3
		printf("Atual: %d\n", atual);
		printf("Ant: %d\n", ant);
		/*/
		atual = procuraEntreFilhos(ant, palavra[i]);
		//printf("Atual: %d\n", atual);


		

		if (atual != NULL){
			i++;
			ant = atual;
		} else {
			break;
		}
	}
	
	if (i == tamanhoDaPalavra){
		imprimeIndices(ant);
	} else {
		printf("-1\n");
	}

}

void procuraEImprimePalavrasTrie (int numeroDePalavras, No *trie, char *palavras[]){
	char palavraParaProcurar[60];
	int i;
	for (i = 0; i < numeroDePalavras; i++){
		strcpy(palavraParaProcurar, palavras[i]);
		int tamanhoDaPalavra = strlen(palavraParaProcurar);
		buscaImprimeTrie(trie, palavraParaProcurar);
	}
}

void pegaPalavras (int numeroDePalavras, char *palavras[]){
	int numeroDaPalavra = 0;
	int letra = 0;
	while (numeroDaPalavra + 1 <= numeroDePalavras){
		scanf("%s", palavras[numeroDaPalavra]);
		numeroDaPalavra++;
	}
}



int main (void){
	int i = 0;
	char texto[MAX];

	char **palavras = (char**)malloc(130*sizeof(char*));
	for(i = 0; i < 130; i++){
        palavras[i] = (char*)malloc(130*sizeof(char));
    }

	int numeroDePalavras = 0;
	int tamanhoDoTexto = 0;

	//imprimeTexto(tamanhoDoTexto, texto);

	// Trie:
	No *trie = criaTrie();
	scanf("%[^\n]s", &texto);
	//scanf("%s\n", &texto);
	tamanhoDoTexto = strlen(texto);
	scanf("%d", &numeroDePalavras);
	pegaPalavras (numeroDePalavras, palavras);
	montaTrie(trie, numeroDePalavras, texto, palavras, tamanhoDoTexto);
	procuraEImprimePalavrasTrie (numeroDePalavras, trie, palavras);
	return 0;
}
