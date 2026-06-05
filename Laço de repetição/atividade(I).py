cont = 1
atual = 1
anterior = 0
while cont <= 15:
    print("Sequência de Fibonacci até o décimo quinto termo:",atual)
    proximo = atual + anterior
    anterior = atual
    atual = proximo
    cont = cont + 1
