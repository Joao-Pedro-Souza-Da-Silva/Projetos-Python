a = [0] * 15
b = [0] * 15
print("Digite 15 valores: ")
for cont in range (15):
    a[cont] = int(input())
    b[cont] = a[cont] ** 2
    print("O quadrado de",a[cont],"é",b[cont])