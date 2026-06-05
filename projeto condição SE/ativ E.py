import math
a = float(input("Digite o valor do coeficiente A: "))
b = float(input("Digite o valor do coeficiente B: "))
c = float(input("Digite o valor do coeficiente C: "))
d = b**2 - (4 * a * c)
print("Delta = ",d)
if d > 0:
    x1 = -b + math.sqrt(d)/(2 * a)
    x2 = -b - math.sqrt(d)/(2 * a)
    print("x1 = ",x1)
    print("x2 = ",x2)
elif d == 0:
    x = -b/(2 * a)
    print("x = ",x)
else:
    print("Não existem raízes reais.")
