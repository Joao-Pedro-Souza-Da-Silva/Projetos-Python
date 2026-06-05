a = [0] * 20
b = [0] * 20
c = [0] * 20
print("Digite 20 valores: ")
for cont in range(20):
   a[cont] = float(input())
for cont in range(20):
   b[cont] = float(input())
   c[cont] = a[cont] - b[cont]
print("Resultado:",c)

