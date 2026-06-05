nome = str(input("Digite o nome: "))
sexo = int(input("Digite 1.Masculino 2.Feminino: "))
if sexo == 1:
    print("Ilmo Sr.",nome)
    print("Masculino")
elif sexo == 2:
    print("Ilma Sra.",nome)
    print("Feminino")
else:
    print("Sexo inválido")
