n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
n4 = float(input("Digite a quarta nota: "))
md1 = (n1+n2+n3+n4)/4
if md1 >= 7:
    print("Aprovado")
else:
    ne = float(input("Digite a nota do exame: "))
    md2 = (md1 + ne)
    if md2 >= 7:
        print("Aprovado")
    else:
        print("Reprovado")
