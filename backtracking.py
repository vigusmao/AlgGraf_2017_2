def listar_permutacoes(n):

    ja_foi_usado = [False] * (n+1)

    def busca_prof(estado_corrente):
        # visite o vertice v: preciso fazer algo especial?
        if len(estado_corrente) == n:
            print(estado_corrente)
            return

        # para cada candidato a ser um vizinho w de v...
        for candidato in range(1, n+1):
            
            if ja_foi_usado[candidato] == False and \
               candidato != len(estado_corrente) + 1:
                # encontrei um vizinho w

                # expando o estado corrente
                estado_corrente.append(candidato)
                ja_foi_usado[candidato] = True

                # chamo recursivamente
                busca_prof(estado_corrente)

                # desfaco a modificacao que tinha sido feita
                estado_corrente.pop()
                ja_foi_usado[candidato] = False

    # ----------

    busca_prof([])
        
    
                
        

        
