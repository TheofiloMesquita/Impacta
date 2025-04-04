numero = int(input())

print(numero)

i = 0
fatorial = 1

while i < numero:
    fatorial *= numero
    numero -=1

print(fatorial)