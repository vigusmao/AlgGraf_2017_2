def criar_grafo(n):
    lista_adjacencias = []
    for i in range(n+1):
        lista_vazia = []
        lista_adjacencias.append(lista_vazia)
    return lista_adjacencias

'''
   parametros:
       G: uma lista de adjacencias (lista de listas de vizinhos)
       vertice1, vertice2: os extremos da nova aresta
'''
def adicionar_aresta(G, vertice1, vertice2):
    G[vertice1].append(vertice2)
    G[vertice2].append(vertice1)


def determinar_articulacoes(G):
    n = len(G) - 1
    pai = [None] * (n+1)
    prof_entrada = [None] * (n+1)
    prof_saida = [None] * (n+1)
    raiz = 1
    pai[raiz] = raiz
    low = [None] + [j for j in range(1, n+1)]
    demarcador = [None] + [False] * n
    articulacao = [None] + [False] * n
    global pe
    global ps
    pe = 1
    ps = 1

    def busca_prof(v):
        global pe
        global ps
        
        # visite o vertice v
        prof_entrada[v] = pe
        pe = pe + 1

        for w in G[v]:
            if pai[w] is None:
                pai[w] = v
                busca_prof(w)

                # visite aresta de arvore (v,w)
                print("visita aresta de arvore %d,%d" % (v,w))
                if prof_entrada[low[w]] < prof_entrada[low[v]]:
                    low[v] = low[w]
                if demarcador[w] == True and v != raiz:
                    articulacao[v] = True
            else:
                if prof_saida[w] is None and pai[v] != w:
                    # visite aresta de retorno (v,w)
                    print("visita aresta de retorno %d,%d" % (v,w))
                    if prof_entrada[w] < prof_entrada[low[v]]:
                        low[v] = w

        prof_saida[v] = ps
        ps = ps + 1
        if low[v] == v or low[v] == pai[v]:
            demarcador[v] = True
            
    # --------

    # faz a chamada original ao busca_prof()
    busca_prof(raiz)

    cont_filhos_raiz = 0
    for v in range(1, n+1):
        if v != raiz and pai[v] == raiz:
            cont_filhos_raiz += 1
    if cont_filhos_raiz >= 2:
        articulacao[raiz] = True

    lista_articulacoes = []
    for v in range(1, n+1):
        if articulacao[v] == True:
            lista_articulacoes.append(v)
    
    return lista_articulacoes
    
# Main

grafo = criar_grafo(6)
arestas = [(1,2),
           (1,3),
           (3,4),
           (3,5),
           (5,6),
           (3,6),
           (1,5)]
for aresta in arestas:
    adicionar_aresta(grafo, aresta[0], aresta[1])








    

