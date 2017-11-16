import sys

def seq_enumeracao(n):
    cont_sequencias = 0
    
    for x in range(0, 2**n):
        binario = bin(x)[2:]
        ok = True
        for i in range(0, len(binario)-1):
            if binario[i]=='1' and binario[i+1]=='1':
                ok = False
                break
        if ok:
            cont_sequencias += 1
            
    return cont_sequencias


def seq_backtracking(n):

    global cont
    cont = 0

    # ----------------------
    def backtrack(estado_corrente):
        global cont
        if len(estado_corrente) == n:
            cont += 1
            return

        for novo_bit in [0,1]:
            posso_acrescentar = (novo_bit == 0) or \
               len(estado_corrente) == 0 or \
               estado_corrente[-1] == 0
            
            if posso_acrescentar:
                estado_corrente.append(novo_bit)
                backtrack(estado_corrente)
                estado_corrente.pop()

    #-----------------------
    
    backtrack([])  # chamada original (lista vazia como estado inicial)
    return cont



def seq_recursivo(n):
    if n == 2:
        return 3
    if n == 1:
        return 2
    return seq_recursivo(n-1) + seq_recursivo(n-2)



memo = {}
def seq_recursivo_memo(n):
    resultado_from_memo = memo.get(n)
    if resultado_from_memo is not None:
        return resultado_from_memo
    
    if n == 2:
        resultado = 3
    elif n == 1:
        resultado = 2
    else:
        resultado = seq_recursivo_memo(n-1) + \
                    seq_recursivo_memo(n-2)

    memo[n] = resultado
    return resultado




