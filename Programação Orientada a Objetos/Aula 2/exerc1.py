while true:
    numero_de_primos = []
    i = 0
    cont = 0
    numero = 2
    while i <= numero: 
        if (numero % i == 0):
            cont+=1
            i+=1
            
    if(cont == 2):
        numero_de_primos.append(numero)
        numero+=1
        break