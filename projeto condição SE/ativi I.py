a = int(input("Digite um valor para A: "))
b = int(input("Digite um valor para B: "))
c = int(input("Digite um valor para C: "))
d = int(input("Digite um valor para D: "))
e = int(input("Digite um valor para E: "))
if a > b and a > c and a > d and a > e:
    print("A é o maior número:",a)
elif a < b and a < c and a < d and a < e:
    print("A é o menor número:",a)
if b > a and b > c and b > d and b > e:
    print("B é o maior número:",b)
elif  b < a and b < c and b < d and b < e:
    print("B é o menor número:",b)
if c > a and c > b and c > d and c > e:
    print("C é o maior número:",c)
elif c < a and c < b and c < d and c < e:
    print("C é o menor número:",c)
if d > a and d > b and d > c and d > e:
    print("D é o maior número:",d)
elif d < a and d < b and d < c and d < e:
    print("D é menor número:",d)
if e > a and e > b and e > c and e > d:
    print("E é o maior número:",e)
elif e < a and e < b and e < c and e < d:
    print("E é o menor número:",e)

