soma = 0
cont1 = 0
cont = 0
for cont in range (1, 16):
    fat = 1
    num = int(input("Digite um valor: "))
    for cont1 in range (1,num + 1):
        fat = fat * cont1
    soma = soma + fat
    print("Resultado da fatorial:",fat)
    print("Resultado da somatória da fatorial:", soma)