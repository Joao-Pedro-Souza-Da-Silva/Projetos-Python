A = [0] * 20
B = [0] * 20
print("Digite 20 valores numéricos: ")
for i in range(20):
    soma = 0
    A[i] = int(input())
    for j in range(1, A[i]+1):
        soma = soma + j
    B[i] = soma
print(B)