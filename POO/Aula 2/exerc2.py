def calcular_medias(notas):
    lista_de_notas = notas
    media = []
    for i in range(len(lista_de_notas)):
        nota_ponderada = []
        for j in range(len(lista_de_notas[0])):
            if(j < 3):
                nota_ponderada.append(lista_de_notas[i][j]*3)
            else:
                nota_ponderada.append(lista_de_notas[i][j]*4)
        media.append((nota_ponderada[0]+nota_ponderada[1]+nota_ponderada[2])/10)
    print(media)

notas_dos_alunos = calcular_medias([[1,2,3],[3,2,1],[10,9,8],[1,7,10]])