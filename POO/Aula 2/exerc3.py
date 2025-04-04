def remover_pares(lista):
    pares = lista
    impares = []
    for i in range(len(pares)):
        if(pares[i] % 2 != 0):
            impares.append(pares[i])
    print(impares)

lista_de_numeros = remover_pares([1,228,543,315,216,934])