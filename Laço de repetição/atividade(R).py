maior = float('-inf')
menor = float('inf')

while True:
    valor = int(input("Digite um valor positivo (ou um valor negativo para sair): "))
    if valor < 0:
        break
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

if maior == float('-inf'):
    print("Nenhum valor positivo foi informado.")
else:
    print("O maior valor informado foi:", maior)
    print("O menor valor informado foi:", menor)
