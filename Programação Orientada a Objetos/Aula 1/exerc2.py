ano = int(input())
if ano % 4 == 0 or ano % 100 == 0 and ano % 400 == 0:
    print("é bissexto")
else:
    print("não é bissexto")
