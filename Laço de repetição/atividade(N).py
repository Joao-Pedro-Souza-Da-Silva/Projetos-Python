soma = 0
cont = 0
num = float(input("Digite um valor: "))
while num >= 0:
    soma += num
    cont += 1
    num = float(input("Digite outro valor: "))

if cont > 0:
    media = soma / cont
    print("Soma:", soma)
    print("Média:", media)
    print("Total de valores lidos:", cont)
else:
    print("Nenhum valor positivo foi lido.")