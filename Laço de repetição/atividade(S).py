dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

quociente = 0
while dividendo >= divisor:
    dividendo -= divisor
    quociente += 1

print("O resultado da divisão é:", quociente)