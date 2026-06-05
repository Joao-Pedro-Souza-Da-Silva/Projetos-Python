a = [0] * 5
b = [0] * 5
c = [0] * 5
d = [0] * 15
for i in range (5):
    a[i] = float(input("Digite um valor para o vetor A: "))
    b[i] = float(input("Digite um valor para o vetor B: "))
    c[i] = float(input("Digite um valor para o vetor C: "))
    d[i] = a [i]
    d[i+5] = b[i]
    d[i+10] = c[i]
print("O resultado da junção dos vetores:",d)

