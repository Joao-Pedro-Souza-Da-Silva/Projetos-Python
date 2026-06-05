nomeA =  str(input("Digite o nome do candidato a: "))
nomeB = str(input("Digite o nome do candidato b: "))
nomeC = str(input("Digite o nome do candidato c: "))
a = int(input("Digite os votos do primeiro candidato:"))
b = int(input("Digite os votos do segundo candidato: "))
c = int(input("Digite os votos do terceiro candidato: "))
n = int(input("Digite os votos nulos: "))
br = int(input("Digite os votos em brancos: "))
t = a+b+c+n+br
a = a/t * 100
b = b/t * 100
c = c/t * 100
print("Candidato",nomeA,": {:.2f}".format(a),"%")
print("Candidato",nomeB,":{:.2f}".format(b), "%")
print("Candidato", nomeC,":{:.2f}".format(c), "%")

