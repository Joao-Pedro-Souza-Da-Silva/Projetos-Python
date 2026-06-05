a = int(input("Digite um valor para A: "))
b = int(input("Digite um valor para B: "))
c = int(input("Digite um valor para C: "))
if c > a and c > b and b > a:
    print("ABC:",a,b,c)
elif a > c and b > c and a > b:
    print("CBA:",c,b,a)
elif b > c and b > a and c > a:
    print("ACB:",a,c,b)
elif c > b and c > a and a > b:
    print("BAC:",b,a,c)
elif a > b and a > c and c > b:
    print("BCA:",b,c,a)
elif b > a and b > c and a > c:
    print("CAB:",c,a,b)

