a = [0] * 15
b = [0] * 15
for cont in range(15):
    a[cont] = int(input("Digite 15 valores: "))
    fat = 1
    for cont1 in range(1,a[cont]+1):
        fat = fat * cont1
    b[cont] = fat
print("A fatorial de",a,"é",b)