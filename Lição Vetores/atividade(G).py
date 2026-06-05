a = [""] * 20
b = [0] * 30
c = [0] * 50

print("Digite 20 nomes:")

for cont in range(20):
    a[cont] = input("Digite o nome " + str(cont+1) + ": ")
    c[cont] = a[cont]

for cont in range(30):
    b[cont] = input("Digite o número " + str(cont+1) + ": ")
    c[cont+20] = b[cont]

print(c)