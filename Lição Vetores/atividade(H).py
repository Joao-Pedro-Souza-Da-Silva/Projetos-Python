a = [0] * 20
b = [0] * 20
j = 19
for i in range(20):
    a[i] = int(input("Digite 20 valores:"))
    b[j] = a[i]
    j = j - 1
print("Elementos do vetor A:",a)
print("Elementos invertidos:",b)