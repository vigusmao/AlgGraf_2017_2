#include <stdlib.h>
#include <stdio.h>

#define NAO_DIRECIONADO 0
#define DIRECIONADO 1

typedef struct _no {
    int vertice;
    struct _no prox;
} NO;

typedef struct {
    NO *primeiro_no;
    NO *ultimo_no;
    int tamanho;
} LISTA_ENCADEADA;

typedef struct {
    int n_vertices;
    int **matriz_adj;
    LISTA_ENCADEADA *lista_adjacencias;
    int tipo;
} GRAFO;

void inicializar_grafo(GRAFO *grafo, int n, int tipo) {
    grafo->n_vertices = n;
    grafo->tipo = tipo;

    // inicializa matriz de adjacencias
    grafo->matriz_adj = (int**) malloc(n * sizeof(int*));
    int linha, coluna;
    for (linha = 0; linha < n; linha++) {
        grafo->matriz_adj[linha] = (int*) malloc(n * sizeof(int));
        for (coluna = 0; coluna < n; coluna++) {
            grafo->matriz_adj[linha][coluna] = 0;
        }
    }

    // inicializa listas de adjacencias
    grafo->lista_adjacencias = (LISTA_ENCADEADA*) malloc (n * sizeof(LISTA_ENCADEADA));
}

void adicionar_aresta(GRAFO *grafo, int origem, int destino) {
    // atualiza matriz de adjacencias
    grafo->matriz_adj[origem][destino] = 1;
    if (grafo->tipo == NAO_DIRECIONADO) {
        grafo->matriz_adj[destino][origem] = 1;
    }

    // atualizando lista de adjacencias

}

void acrescentar_vizinho(LISTA_ENCADEADA *lista, int w) {
    NO *novo_no = (NO*) malloc(sizeof(NO));
    novo_no->vertice = w;
    novo_no->prox = NULL;

    if (lista->tamanho == 0) {
        lista->primeiro_no = novo_no;
    } else {
        lista->ultimo_no->prox = novo_no;
    }
    lista->ultimo_no = novo_no;
    lista->tamanho++;
}

// Retorna 1, se existir a aresta; 0, caso contrario
int eh_aresta(GRAFO *grafo, int origem, int destino) {
    return grafo->matriz_adj[origem][destino];
}

int obter_vizinhos(GRAFO *grafo, int v, int *lista_vizinhos) {
    int n = grafo->n_vertices;
    int cont_vizinhos = 0;
    int w;
    for (w = 0; w < n; w++) {
        if (eh_aresta(grafo, v, w)) {
            if (lista_vizinhos != NULL) {
                lista_vizinhos[cont_vizinhos] = w;
            }
            cont_vizinhos++;
        }
    }
    if (grafo->tipo == DIRECIONADO) {
        for (w = 0; w < n; w++) {
            if (eh_aresta(grafo, w, v)) {
                if (lista_vizinhos != NULL) {
                    lista_vizinhos[cont_vizinhos] = w;
                }
                cont_vizinhos++;
            }
        }
    }
    return cont_vizinhos;
}

void imprimir_grafo(GRAFO *grafo) {
    int n = grafo->n_vertices;
    printf("\n\nNumero de vertices = %d\n", n);
    int linha, coluna;

    // imprime header das colunas
    printf("\n      ");
    for (coluna = 0; coluna < n; coluna++) {
        printf(" %2d ", coluna);
    }
    printf("\n__");
    for (coluna = 0; coluna <= n; coluna++) {
        printf("____");
    }

    for (linha = 0; linha < n; linha++) {
        printf("\n %2d | ", linha);
        for (coluna = 0; coluna < n; coluna++) {
            printf(" %2d ", grafo->matriz_adj[linha][coluna]);
        }
    }
    printf("\n\n");
}

int main() {

    int n = 4;

    GRAFO g;
    inicializar_grafo(&g, n, NAO_DIRECIONADO);

    adicionar_aresta(&g, 1, 2);
    adicionar_aresta(&g, 1, 3);
    adicionar_aresta(&g, 0, 1);
    adicionar_aresta(&g, 2, 3);


    imprimir_grafo(&g);

    int *vizinhos = (int*) malloc(2*n * sizeof(int));
    int n_vizinhos = obter_vizinhos(&g, 1, vizinhos);
    printf("\nNumero de vizinhos do 1 = %d", n_vizinhos);
    printf("\nVizinhos --> [ ");
    int vizinho_idx;
    for (vizinho_idx = 0; vizinho_idx < n_vizinhos; vizinho_idx++) {
        printf("%d ", vizinhos[vizinho_idx]);
    }
    printf("]\n");
}
