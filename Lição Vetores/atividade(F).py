a = [0] * 15
b = [0] * 15
c = [0] * 30
for cont in range(15):
    a[cont] = int(input("Digite para o vetor A: "))
    b[cont] = int(input("Digite para o vetor B: "))
    c[cont] = a [cont]
    c[cont + 15] = b[cont]
print("Resultado da junção dos vetores:",c)