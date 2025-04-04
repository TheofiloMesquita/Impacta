numero = int(input())

cont = 0
while i < numero:
    if(numero % i == 0):
        cont+=1
    numero -= 1

if(cont == 2):
    print(f'O numero {numero} é primo')
else:
    print(f'O numero {numero} não é primo')